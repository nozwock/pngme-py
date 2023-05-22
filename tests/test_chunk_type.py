import unittest

from pngme.chunk_type import ChunkType


class TestChunkType(unittest.TestCase):
    def test_chunk_type_from_bytes(self) -> None:
        expected = [82, 117, 83, 116]
        actual = ChunkType.from_bytes(bytes([82, 117, 83, 116]))

        self.assertEqual(expected, actual.bytes())

    def test_chunk_type_from_str(self) -> None:
        expected = ChunkType.from_bytes(bytes())
        actual = ChunkType.from_str("RuSt")

        self.assertEqual(expected, actual)

    def test_chunk_type_is_critical(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertTrue(chunk.is_critical())

    def test_chunk_type_is_not_critical(self) -> None:
        chunk = ChunkType.from_str("ruSt")
        self.assertFalse(chunk.is_critical())

    def test_chunk_type_is_public(self) -> None:
        chunk = ChunkType.from_str("RUSt")
        self.assertTrue(chunk.is_public())

    def test_chunk_type_is_not_public(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertFalse(chunk.is_public())

    def test_chunk_type_is_reserved_bit_valid(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertTrue(chunk.is_reserved_bit_valid())

    def test_chunk_type_is_reserved_bit_invalid(self) -> None:
        chunk = ChunkType.from_str("Rust")
        self.assertFalse(chunk.is_reserved_bit_valid())

    def test_chunk_type_is_safe_to_copy(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertTrue(chunk.is_safe_to_copy())

    def test_chunk_type_is_unsafe_to_copy(self) -> None:
        chunk = ChunkType.from_str("RuST")
        self.assertFalse(chunk.is_safe_to_copy())

    def test_valid_chunk_is_valid(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertTrue(chunk.is_valid())

        chunk = ChunkType.from_str("ruSt")
        self.assertTrue(chunk.is_valid())

    def test_invalid_chunk_is_valid(self) -> None:
        chunk = ChunkType.from_str("Rust")
        self.assertFalse(chunk.is_valid())

        with self.assertRaises(ValueError):
            chunk = ChunkType.from_str("Ru1t")

    def test_chunk_type_string(self) -> None:
        chunk = ChunkType.from_str("RuSt")
        self.assertEqual(str(chunk), "RuSt")

    def test_chunk_type_trait_impls(self) -> None:
        chunk_type_1 = ChunkType.from_bytes(bytes([82, 117, 83, 116]))
        chunk_type_2 = ChunkType.from_str("RuSt")
        chunk_string = str(chunk_type_1)
        are_chunks_equal = chunk_type_1 == chunk_type_2


if __name__ == "__main__":
    unittest.main()
