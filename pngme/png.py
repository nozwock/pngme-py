from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .chunk import Chunk
from .chunk_type import ChunkType


@dataclass
class Png:
    """A PNG container as described by the PNG spec.
    http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html
    """

    STANDARD_HEADER: bytes = b"header bytes here!"

    ...

    @classmethod
    def from_chunks(cls, chunks: list[Chunk]) -> Png:
        """Creates a `Png` from a list of chunks using the correct header."""

        # Write me!
        raise NotImplementedError

    @classmethod
    def from_path(cls, path: Path) -> Png:
        """Creates a `Png` from a file path."""

        # Write me!
        raise NotImplementedError

    @classmethod
    def from_bytes(cls, value: bytes) -> Png:
        """Tries to create a `Png` instance from a byte sequence."""

        # Write me!
        raise NotImplementedError

    def append_chunk(self, chunk: Chunk) -> None:
        """Appends a chunk to the end of this `Png` file's `Chunk` list."""

        # Write me!
        raise NotImplementedError

    def remove_chunk(self, chunk_type: ChunkType) -> Chunk:
        """Searches for a `Chunk` with the specified `chunk_type` and removes the first matching `Chunk` from this `Png` list of chunks."""

        # Write me!
        raise NotImplementedError

    def header(self) -> bytes:
        """The header of this PNG."""

        # Write me!
        raise NotImplementedError

    def chunks(self) -> list[Chunk]:
        """Lists the `Chunk`s stored in this `Png`."""

        # Write me!
        raise NotImplementedError

    def chunks_by_type(self, chunk_type: ChunkType) -> list[Chunk]:
        """Searches for `Chunk` with the specified `chunk_type` and returns all the matching `Chunk` from this `Png`."""

        # Write me!
        raise NotImplementedError

    def as_bytes(self) -> bytes:
        """Returns this `Png` as a byte sequence."""

        # Write me!
        raise NotImplementedError
