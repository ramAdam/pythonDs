from ds.array import Array2D


class LifeGrid:
    def __init__(self, nrows, ncols):
        pass

    def configure(self, cordlist):
        """takes a list of tuples
           [(2, 3), (1, 2), (4, 3)] and set them alive
        """
        pass

    def clearCell(self, row, col):
        """set index to a dead cell"""
        pass

    def setCell(self, row, col):
        """set index to a live cell"""
        pass

    def numberOfLiveCells(self, row, col):
        """returns a the number of live cell around the index"""
        pass
