import pygame as pg
from typing import Dict

from .helpers.Tile import Tile


class Board:
    def __init__(self, settings: Dict) -> None:
        self.settings = settings["visualizer"]
        self.tile_settings = settings["tilemap"]

        self.screen = pg.display.set_mode(
            (
                self.settings["tiles_in_row"] * self.settings["tile_width"],
                self.settings["tiles_in_col"] * self.settings["tile_height"],
            )
        )

        self.board = [
            [
                Tile(x, y, len(self.tile_settings[self.settings["tilemap_in_use"]]))
                for x in range(self.settings["tiles_in_row"])
            ]
            for y in range(self.settings["tiles_in_col"])
        ]

    def draw_board(self) -> None:
        for row in self.board:
            for tile in row:
                if isinstance(tile.tile, pg.Surface):
                    self.screen.blit(tile.tile, (tile.xIdx, tile.yIdx))
                    continue

                pg.draw.rect(
                    self.screen,
                    tile.tile,
                    pg.Rect(
                        tile.xIdx * self.settings["tile_width"],
                        tile.yIdx * self.settings["tile_height"],
                        self.settings["tile_width"],
                        self.settings["tile_height"],
                    ),
                )
