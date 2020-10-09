from ds.array import Array2D
from itertools import cycle
import pdb


class RotateAroundIterator:
    def __init__(self, array2D: Array2D):
        self._array = array2D
        self._nEnd = self._array.nRows + self._array.nCols
        self._nStart = 1
        self._rowIdx = 0
        self._colIdx = 1

    @property
    def startIdx(self):
        return self._nStart

    @startIdx.setter
    def startIdx(self, value):
        self._nStart = value

    @property
    def endIdx(self):
        return self._nEnd

    @endIdx.setter
    def endIdx(self, value):
        self._nEnd = value

    @property
    def northEast(self):
        return self._array.nCols

    @property
    def southEast(self):
        return self.endIdx

    @property
    def southWest(self):
        return self.endIdx + self._array.nCols

    @property
    def northWest(self):
        return self.endIdx + self._array.nCols + self._array.nRows

    def __next__(self):
        value = 0
        if self._arrayLengthIsOne():
            raise StopIteration
        if self.startIdx <= self.northWest:

            if self.startIdx < self.northEast:
                self._raiseNWtoNEIndexError()
                if self._colIdx + 1 < self.northEast:
                    value = self._array[self._rowIdx, self._colIdx]
                    self._colIdx += 1

            if self.startIdx >= self.northEast and self.startIdx < self.southEast:
                assert self._colIdx < self.northEast
                if self._rowIdx + 1 < self._array.nRows:
                    self._rowIdx += 1
                    value = self._array[self._rowIdx, self._colIdx]

            if self.startIdx >= self.southEast and self.startIdx < self.southWest:

                assert self._colIdx >= 0, self._rowIdx == self._array.nRows - 1

                if self._colIdx - 1 >= 0:
                    self._colIdx -= 1
                    value = self._array[self._rowIdx, self._colIdx]

            if self.startIdx >= self.southWest and self.startIdx <= self.northWest:
                if self._rowIdx - 1 >= 0:
                    self._rowIdx -= 1
                    value = self._array[self._rowIdx, self._colIdx]

            self.startIdx += 1
            return value

        else:
            raise StopIteration

    def __iter__(self):
        return self

    def _arrayLengthIsOne(self):
        """return True for the 2D array of length one"""
        if self._array.nRows == 1 and self._array.nCols == 1:
            return True
        return False

    def _raiseColIdxError(self):
        """raises a column index error if column index is
           is greater than or equal to north east cornor of
           array
        """
        assert self._colIdx < self.northEast, "Column index {} == North East Index {}".format(
            self._colIdx, self.northEast)

    def _raiseNWtoNEIndexError(self):
        if self._colIdx >= self.northEast and self._rowIdx != 0:
            raise IndexError


class SorroundingCellIterator:
    def __init__(self, grid, row, col):
        self._grid = grid
        self._rowIdx = row
        self._colIdx = col

    def __next__(self):
        return (self._rowIdx, self._colIdx)

    def __iter__(self):
        return self


class LifeGrid(Array2D):
    def __init__(self, nrows, ncols):
        """Setup a 2d grid with initial config set to 0"""
        super(LifeGrid, self).__init__(nrows, ncols)
        self.clear(0)

    def configure(self, cordlist):
        """takes a list of tuples
           [(2, 3), (1, 2), (4, 3)] and set them alive
        """
        try:
            for row in cordlist:
                i, j = row
                self[i, j] = 1
        except Exception as e:
            print(e.__cause__)

    def clearCell(self, row, col):
        """set index to a dead cell"""
        try:
            self[row, col] = 0
        except IndexError as error:
            print(error.__cause__)

    def setCell(self, row, col):
        """set index to a live cell"""
        try:
            self[row, col] = 1
        except IndexError as error:
            print(error.__cause__)

    def numberOfLiveCells(self, row, col):
        """returns a the number of live cell around the index"""
        ix, jy = row - 1, col - 1
        reset = jy

        length = 3
        count = 0

        for _ in range(length):
            for _ in range(length):
                try:
                    if not (ix == row and jy == col):
                        if self[ix, jy] == 1:
                            count += 1
                    jy += 1
                except AssertionError:
                    jy += 1
            ix += 1
            jy = reset
        return count
