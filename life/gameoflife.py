from life import LifeGrid
from enum import IntEnum


def main():
    pass


def evolve(grid: LifeGrid):
    Cell: IntEnum = IntEnum('Cell', {'DEAD': 0, 'ALIVE': 1})
    idxs = {}
    for i in range(grid.nRows):
        for j in range(grid.nCols):
            if grid[i, j] == Cell.ALIVE and grid.numberOfLiveCells(i, j) <= 1:
                idxs[(i, j)] = 0
            elif grid[i, j] == Cell.ALIVE and grid.numberOfLiveCells(i, j) >= 4:
                idxs[i, j] = 0
            elif grid[i, j] == Cell.DEAD and grid.numberOfLiveCells(i, j) == 3:
                idxs[i, j] = 1
            elif grid[i, j] == Cell.ALIVE and (grid.numberOfLiveCells(i, j) == 2 or grid.numberOfLiveCells(i, j) == 3):
                idxs[(i, j)] = 1
    for key, value in idxs.items():
        grid[key] = value


def draw(grid):
    print(grid)


if __name__ == "__main__":
    N_GEN = 4
    CONFIG_1 = [(3, 5), (3, 6), (4, 7)]
    CONFIG_2 = [(3, 5), (3, 6), (4, 6)]
    CONFIG_3 = [(3, 5), (3, 6), (3, 7)]

    grid = LifeGrid(7, 9)
    grid.configure(CONFIG_1)

    for i in range(N_GEN):
        draw(grid)
        evolve(grid)
