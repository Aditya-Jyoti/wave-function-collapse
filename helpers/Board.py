import pygame as pg
from typing import Dict

from .Cell import Cell


class Board:
    def __init__(self, settings: Dict) -> None:
        self.settings = settings["visualizer"]
        self.tile_settings = settings["tilemap"]

        self.screen = pg.display.set_mode(
            (
                self.settings["cells_in_row"] * self.settings["cell_width"],
                self.settings["cells_in_col"] * self.settings["cell_height"],
            )
        )

        self.board = [
            [Cell(x, y, 9999) for x in range(self.settings["cells_in_row"])]
            for y in range(self.settings["cells_in_col"])
        ]

    def draw_board(self) -> None:
        for row in self.board:
            for cell in row:
                if cell.tile is not None:
                    self.screen.blit(
                        cell.tile.img,
                        (
                            cell.xIdx * self.settings["cell_width"],
                            cell.yIdx * self.settings["cell_height"],
                        ),
                    )
                    continue

                pg.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    pg.Rect(
                        cell.xIdx * self.settings["cell_width"],
                        cell.yIdx * self.settings["cell_height"],
                        self.settings["cell_width"],
                        self.settings["cell_height"],
                    ),
                )

    def __str__(self) -> str:
        return_str = ""

        for row in self.board:
            return_str += ", ".join([repr(cell) for cell in row])
            return_str += "\n"

        return return_str
