import struct
import unittest

from pngme.chunk import Chunk
from pngme.chunk_type import ChunkType


class TestChunk(unittest.TestCase):
    def test_new_chunk(self) -> None:
        chunk_type = ChunkType.from_bytes(b"RuSt")
        data = b"This is where your secret message will be!"
        chunk = Chunk.new(chunk_type, data)

        self.assertEqual(chunk.length(), 42)
        self.assertEqual(chunk.chunk_type(), chunk_type)
        self.assertEqual(
            chunk.data_as_string(), "This is where your secret message will be!"
        )
        self.assertEqual(chunk.crc(), 2882656334)

    def test_chunk_length(self) -> None:
        chunk = self._create_testing_chunk()
        self.assertEqual(chunk.length(), 42)

    def test_chunk_type(self) -> None:
        chunk = self._create_testing_chunk()
        self.assertEqual(str(chunk.chunk_type()), "RuSt")

    def test_chunk_string(self) -> None:
        chunk = self._create_testing_chunk()
        chunk_string = chunk.data_as_string()
        expected_chunk_string = "This is where your secret message will be!"
        self.assertEqual(chunk_string, expected_chunk_string)

    def test_chunk_crc(self) -> None:
        chunk = self._create_testing_chunk()
        self.assertEqual(chunk.crc(), 2882656334)

    def test_valid_chunk_from_bytes(self) -> None:
        data_length = 42
        chunk_type = b"RuSt"
        message_bytes = b"This is where your secret message will be!"
        crc = 2882656334

        chunk_data = (
            struct.pack(">I", data_length)
            + chunk_type
            + message_bytes
            + struct.pack(">I", crc)
        )

        chunk = Chunk.from_bytes(chunk_data)

        chunk_string = chunk.data_as_string()
        expected_chunk_string = "This is where your secret message will be!"

        self.assertEqual(chunk.length(), 42)
        self.assertEqual(str(chunk.chunk_type()), "RuSt")
        self.assertEqual(chunk_string, expected_chunk_string)
        self.assertEqual(chunk.crc(), 2882656334)

    def test_invalid_chunk_from_bytes(self) -> None:
        data_length = 42
        chunk_type = b"RuSt"
        message_bytes = b"This is where your secret message will be!"
        crc = 2882656333

        chunk_data = (
            struct.pack(">I", data_length)
            + chunk_type
            + message_bytes
            + struct.pack(">I", crc)
        )

        with self.assertRaises(ValueError):
            Chunk.from_bytes(chunk_data)

    def test_chunk_trait_impls(self) -> None:
        data_length = 42
        chunk_type = b"RuSt"
        message_bytes = b"This is where your secret message will be!"
        crc = 2882656334

        chunk_data = (
            struct.pack(">I", data_length)
            + chunk_type
            + message_bytes
            + struct.pack(">I", crc)
        )

        chunk = Chunk.from_bytes(chunk_data)

        _ = str(chunk)

    def _create_testing_chunk(self) -> Chunk:
        data_length = 42
        chunk_type = ChunkType.from_bytes(b"RuSt")
        message_bytes = b"This is where your secret message will be!"
        crc = 2882656334

        chunk_data = (
            struct.pack(">I", data_length)
            # Big-endian bytes iterable
            # https://docs.python.org/2/library/struct.html#format-strings
            + chunk_type.bytes()
            + message_bytes
            + struct.pack(">I", crc)
        )

        return Chunk.from_bytes(chunk_data)


if __name__ == "__main__":
    unittest.main()
