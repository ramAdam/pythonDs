import unittest
from linalg import Matrix
from data import matrix, other, result, subtractResult, spareMatrix, scaledMatrix
from ds.array import Array
from copy import copy
import pdb


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.ncols = 2
        self.nrows = 3

    def testClear(self):
        for row in spareMatrix:
            for i in range(len(row)):
                assert row[i] == 0

    def testNumRows(self):
        assert matrix.numRows() == self.nrows

    def testNumOfCols(self):
        assert matrix.numCols() == self.ncols

    def testEqual(self):
        assert not matrix == other
        assert matrix == matrix

    def testSubtract(self):
        "subtract matrices should return a new subtracted matrix"
        result = matrix - other
        assert result == subtractResult

    def testColRowEqual(self):
        assert matrix.colsRowsEqual(copy(matrix))

    def testEquals(self):
        assert matrix == copy(matrix)

    def testAdd(self):
        testResult = matrix + other
        assert testResult == result

    def testscaleBy(self):
        matrix * 2
        assert matrix == scaledMatrix

    def testTranspose(self):
        pass
