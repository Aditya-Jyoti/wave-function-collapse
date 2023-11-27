from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from .Tile import Tile


@dataclass
class Cell:
    xIdx: int
    yIdx: int
    entropy: int

    tile: Optional[Tile] = None
    matching_tiles: Optional[List[Tile]] = None

    def get_neighbours(self, board: List[List[Cell]]) -> List[Cell]:
        return [
            board[self.yIdx + y][self.xIdx + x]
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]
            if 0 <= self.xIdx + x < len(board[0]) and 0 <= self.yIdx + y < len(board)
        ]

    def __repr__(self) -> str:
        return f"Cell(({self.xIdx, self.yIdx}), entropy= {self.entropy})"
