from dataclasses import dataclass

from .chunk_type import ChunkType


@dataclass
class Chunk:
    """
    A validated PNG chunk. See the PNG Spec for more details.
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html#Chunk-layout
    """

    ...

    @classmethod
    def new(cls, chunk_type: ChunkType, data: bytes) -> Chunk:
        # Write me!
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, value: bytes) -> Chunk:
        # Write me!
        raise NotImplementedError

    def length(self) -> int:
        """The length of the data portion of this chunk."""

        # Write me!
        raise NotImplementedError

    def chunk_type(self) -> ChunkType:
        """The `ChunkType` of this chunk."""

        # Write me!
        raise NotImplementedError

    def data(self) -> bytes:
        """The raw data contained in this chunk in bytes."""

        # Write me!
        raise NotImplementedError

    def crc(self) -> int:
        """The CRC of this chunk."""

        # Write me!
        raise NotImplementedError

    def data_as_string(self) -> str:
        """Returns the data stored in this chunk as a `String`. This function will return an error
        if the stored data is not valid UTF-8.
        """

        # Write me!
        raise NotImplementedError

    def as_bytes(self) -> bytes:
        """Returns this chunk as a byte sequences described by the PNG spec.
        The following data is included in this byte sequence in order:
        1. Length of the data *(4 bytes)*
        2. Chunk type *(4 bytes)*
        3. The data itself *(`length` bytes)*
        4. The CRC of the chunk type and data *(4 bytes)*"""

        # Write me!
        raise NotImplementedError

    def __str__(self) -> str:
        # Write me!
        raise NotImplementedError
