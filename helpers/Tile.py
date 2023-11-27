from __future__ import annotations

import pygame as pg

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Tile:
    img: pg.Surface
    rule: List[int]

    def rotate_tile(self, angle: int) -> None:
        if angle == 0:
            return
        
        self.img = pg.transform.rotate(self.img, angle)
        self.rule = self.rule[-angle // 90 :] + self.rule[: 4 - (angle // 90)]

    @staticmethod
    def total_tiles(settings: Dict) -> List[Tile]:
        tilemap_in_use = settings["visualizer"]["tilemap_in_use"]

        base_tiles = [
            Tile(
                pg.transform.scale(
                    pg.image.load(f"assets/{tilemap_in_use}/{img}.png"),
                    (
                        settings["visualizer"]["cell_width"],
                        settings["visualizer"]["cell_height"],
                    ),
                ),
                rule,
            )
            for img, rule in settings["tilemap"][tilemap_in_use].items()
        ]

        total_tiles = []

        for tile in base_tiles:
            for angle in [0, 90, 180, 270]:
                tile.rotate_tile(angle)
                total_tiles.append(tile)

        return total_tiles

    def __repr__(self) -> str:
        return f"Tile({self.rule=})"
