from __future__ import annotations

from dataclasses import dataclass

from typing import Union, Tuple, List
import pygame as pg


@dataclass
class Tile:
    xIdx: int
    yIdx: int
    entropy: int

    tile: Union[Tuple, pg.Surface] = (255, 255, 255)

    def get_neighbours(self, board: List[List[Tile]]) -> List[Tile]:
        return [
            board[self.yIdx + y][self.xIdx + x]
            for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]
            if 0 <= self.xIdx + x < len(board[0]) and 0 <= self.yIdx + y < len(board)
        ]
