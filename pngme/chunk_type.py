from dataclasses import dataclass


@dataclass
class ChunkType:
    """
    A validated PNG chunk type. See the PNG spec for more details.
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-naming-conventions
    """

    ...

    # this is `try_from` mentioned in the tutorial
    @classmethod
    def from_bytes(cls, value: bytes) -> ChunkType:
        # Write me!
        raise NotImplementedError

    @classmethod
    def from_str(cls, s: str) -> ChunkType:
        # Write me!
        raise NotImplementedError

    def bytes(self) -> bytes:
        """Returns the raw bytes contained in this chunk."""

        # Write me!
        raise NotImplementedError

    def is_critical(self) -> bool:
        """Returns the property state of the first byte as described in the PNG spec."""

        # Write me!
        raise NotImplementedError

    def is_public(self) -> bool:
        """Returns the property state of the second byte as described in the PNG spec."""

        # Write me!
        raise NotImplementedError

    def is_reserved_bit_valid(self) -> bool:
        """Returns the property state of the third byte as described in the PNG spec."""

        # Write me!
        raise NotImplementedError

    def is_safe_to_copy(self) -> bool:
        """Returns the property state of the fourth byte as described in the PNG spec."""

        # Write me!
        raise NotImplementedError

    def is_valid(self) -> bool:
        """Returns true if the reserved byte is valid.
        Note that this chunk type should always be valid as it is validated during construction.
        """

        # Write me!
        raise NotImplementedError

    @staticmethod
    def is_valid_byte(byte: int) -> bool:
        """Valid bytes are represented by the characters A-Z or a-z."""

        # Write me!
        raise NotImplementedError

    def __str__(self) -> str:
        # Write me!
        raise NotImplementedError
