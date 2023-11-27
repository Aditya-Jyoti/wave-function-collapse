import tomllib

import pygame as pg
from itertools import chain
from random import choice
from typing import Dict, List

from helpers.Board import Board
from helpers.Cell import Cell
from helpers.Tile import Tile

with open("settings.toml", "rb") as settings_file:
    SETTINGS = tomllib.load(settings_file)

TOTAL_TILES = Tile.total_tiles(SETTINGS)
print(len(TOTAL_TILES))


traversed_cell_coordinates = set()


def get_matching_tile(parent_cell: Cell, neighbours: List[Cell]) -> List[Tile]:
    matching_tile = []

    for tile in TOTAL_TILES:
        for cell in neighbours:
            if not cell.tile:
                continue

            if cell.xIdx == parent_cell.xIdx:
                if cell.yIdx < parent_cell.yIdx:  # top
                    if tile.rule[2] == cell.tile.rule[0]:
                        matching_tile.append(tile)
                        continue

                elif cell.yIdx > parent_cell.yIdx:  # bottom
                    if tile.rule[0] == cell.tile.rule[2]:
                        matching_tile.append(tile)
                        continue

            elif cell.yIdx == parent_cell.yIdx:
                if cell.xIdx < parent_cell.xIdx:  # left
                    if tile.rule[3] == cell.tile.rule[1]:
                        matching_tile.append(tile)
                        continue

                elif cell.xIdx > parent_cell.xIdx:  # right
                    if tile.rule[1] == cell.tile.rule[3]:
                        matching_tile.append(tile)
                        continue

    return matching_tile


def collapse(board: List[List[Cell]]) -> List[List[Cell]]:
    current_cell = min(chain.from_iterable(board), key=lambda cell: cell.entropy)

    if (
        (
            current_cell.xIdx,
            current_cell.yIdx,
        )
        in traversed_cell_coordinates
        or not current_cell.matching_tiles
        or current_cell.entropy == 9999
    ):
        return board

    traversed_cell_coordinates.add((current_cell.xIdx, current_cell.yIdx))
    current_cell.tile = choice(current_cell.matching_tiles)

    cell_neighbours = current_cell.get_neighbours(board)
    for cell in cell_neighbours:
        if (cell.xIdx, cell.yIdx) in traversed_cell_coordinates:
            continue

        cell.matching_tiles = get_matching_tile(cell, cell.get_neighbours(board))
        cell.entropy = len(cell.matching_tiles)

    current_cell.entropy = 9999

    return collapse(board)


def main_loop(settings: Dict):
    board = Board(settings)
    clock = pg.time.Clock()

    start_tile = board.board[settings["visualizer"]["cells_in_col"] // 2][
        settings["visualizer"]["cells_in_row"] // 2
    ]

    start_tile.tile = choice(TOTAL_TILES)
    start_tile.matching_tiles = TOTAL_TILES
    start_tile.entropy = len(start_tile.matching_tiles)

    cell_neighbours = start_tile.get_neighbours(board.board)
    for cell in cell_neighbours:
        cell.matching_tiles = get_matching_tile(cell, cell.get_neighbours(board.board))
        cell.entropy = len(cell.matching_tiles)

    board.board = collapse(board.board)
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        board.draw_board()
        clock.tick(settings["visualizer"]["fps"])
        pg.display.update()


if __name__ == "__main__":
    print("Wave Function Collapse")
    print("Visualizer for the wave function collapse algorithm")
    print("Author: Aditya Jyoti")

    pg.init()
    pg.display.set_caption("wave function collapse")

    main_loop(SETTINGS)

    pg.quit()
