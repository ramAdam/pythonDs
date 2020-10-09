import unittest

from life import LifeGrid, SorroundingCellIterator, RotateAroundIterator
from life import evolve
from ds import Array2D
from data import rotArray
import pdb


class TestLifeGrid(unittest.TestCase):
    def setUp(self):
        self.nrows = 10
        self.ncols = 10
        self.initialConfig = [(0, 0), (9, 0), (8, 0), (1, 9), (0, 9), (0, 8), (9, 9), (8, 9),
                              (1, 0), (2, 3), (1, 2), (4, 3)]
        self.lifeGrid = LifeGrid(self.nrows, self.ncols)

    def testConfigure(self):
        self.lifeGrid.configure(self.initialConfig)
        for row in self.initialConfig:
            i, j = row
            assert self.lifeGrid[i, j] == 1
        self.lifeGrid.clear(0)

    def testClearCell(self):
        self.lifeGrid.configure(self.initialConfig)
        self.lifeGrid.clearCell(5, 2)
        self.lifeGrid.clearCell(4, 3)
        self.lifeGrid[4, 3] == 0
        self.lifeGrid[5, 2] == 0
        self.lifeGrid.clear(0)

    def testSetCell(self):
        self.lifeGrid.configure(self.initialConfig)
        self.lifeGrid.setCell(5, 2)
        assert self.lifeGrid[5, 2] == 1
        self.lifeGrid.clear(0)

    def testNumberOfLiveCells(self):
        self.lifeGrid.configure(self.initialConfig)
        assert self.lifeGrid.numberOfLiveCells(0, 0) == 1
        assert self.lifeGrid.numberOfLiveCells(9, 0) == 1
        assert self.lifeGrid.numberOfLiveCells(0, 9) == 2
        assert self.lifeGrid.numberOfLiveCells(9, 9) == 1
        assert self.lifeGrid.numberOfLiveCells(2, 3) == 1
        assert self.lifeGrid.numberOfLiveCells(1, 2) == 1
        assert self.lifeGrid.numberOfLiveCells(4, 3) == 0
        self.lifeGrid.clear(0)


class TestSoroundingCellIterator(unittest.TestCase):
    def setUp(self):
        self.nrows = 10
        self.ncols = 10
        self.initialConfig = [(2, 3), (1, 2), (4, 3)]
        self.grid = LifeGrid(self.nrows, self.ncols)
        self.cellIter = SorroundingCellIterator(self.grid, 2, 3)

    def testNext(self):
        assert next(iter(self.cellIter)) == (2, 3)


class TestRotationIterator(unittest.TestCase):
    def setUp(self):
        self.array = Array2D(1, 1)
        self.arrayB = Array2D(10, 6)
        self.arrayB.clear(0)
        self.rotatorB = RotateAroundIterator(rotArray)

    def testArrayOfLengthOne(self):
        rIter = RotateAroundIterator(self.array)
        assert rIter._arrayLengthIsOne()

    def testNextRaiseStopIteration(self):
        """raises stop iteration with array of length one"""
        rotator = RotateAroundIterator(self.array)
        self.assertRaises(StopIteration, rotator.__next__)

    def testStartAndEndIdxProperty(self):
        assert self.rotatorB.startIdx == 1
        assert self.rotatorB.endIdx == 16

    def testStartIdxGreaterThanEndIdx(self):
        """iteration should stop if start index is greater than end
           end index
        """
        for i in range(1, self.rotatorB.northWest + 2):
            if i > self.rotatorB.northWest:
                self.assertRaises(StopIteration, self.rotatorB.__next__)
            else:
                self.rotatorB.__next__()

    def testCorners(self):
        assert self.rotatorB.northEast == 6
        assert self.rotatorB.southEast == 16
        assert self.rotatorB.southWest == 22
        assert self.rotatorB.northWest == 32

    def testColIndexFromNorthWestToNorthNorthEast(self):
        """From NW to NE column index should always be less than 
           north east corner
        """

        self.rotatorB._colIdx == 1
        assert self.rotatorB._rowIdx == 0

        for _ in range(1, self.rotatorB.northEast):
            self.rotatorB.__next__()

        assert self.rotatorB.startIdx == 6
        assert self.rotatorB._colIdx == 5
        assert self.rotatorB._rowIdx == 0

        for _ in range(self.rotatorB.startIdx, self.rotatorB.southEast):
            self.rotatorB.__next__()

        assert self.rotatorB.startIdx == 16
        assert self.rotatorB._colIdx == 5
        assert self.rotatorB._rowIdx == 9

        for _ in range(self.rotatorB.startIdx, self.rotatorB.southWest):
            self.rotatorB.__next__()

        assert self.rotatorB.startIdx == 22
        assert self.rotatorB._colIdx == 0
        assert self.rotatorB._rowIdx == 9

        for _ in range(self.rotatorB.startIdx, self.rotatorB.northWest):
            self.rotatorB.__next__()

        assert self.rotatorB.startIdx == 32
        assert self.rotatorB._colIdx == 0
        assert self.rotatorB._rowIdx == 0


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.grid = LifeGrid(10, 10)

    def testEvolveAliveCellsLessThanOrEqualToOne(self):
        """when number of live cells are less than or equal to one"""
        initialConfig = [(0, 0), (1, 0)]
        self.grid.configure(initialConfig)
        evolve(self.grid)
        for i, j in initialConfig:
            assert self.grid[i, j] == 0

        self.grid.clear(0)

    def testEvolveAliveCellsGreaterThanEqualToFour(self):
        """when number of live cells are greater than equal to four, the cell should be dead"""
        initialConfig = [(1, 0), (0, 0), (0, 1), (1, 1), (2, 0)]
        self.grid.configure(initialConfig)

        evolve(self.grid)
        assert self.grid[0, 0] == 1

        assert self.grid[0, 0] == 1
        assert self.grid[1, 0] == 0
        assert self.grid[1, 1] == 1
        assert self.grid[2, 0] == 0

    def testDraw(self):
        pass
