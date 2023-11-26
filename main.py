import tomllib

import pygame as pg
from typing import Dict

from helpers.Board import Board
from helpers.Tile import Tile

with open("settings.toml", "rb") as settings_file:
    SETTINGS = tomllib.load(settings_file)

TOTAL_TILES = Tile.total_tiles(SETTINGS)


def collapse():
    ...


def main_loop(settings: Dict):
    board = Board(settings)

    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        board.draw_board()
        clock.tick(settings["visualizer"]["fps"])
        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    print("Wave Function Collapse")
    print("Visualizer for the wave function collapse algorithm")
    print("Author: Aditya Jyoti")

    pg.init()
    pg.display.set_caption("wave function collapse")

    main_loop(SETTINGS)
