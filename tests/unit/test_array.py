import unittest
from ds.array import Array, Array2D
import pdb


class TestArray(unittest.TestCase):
    def setUp(self):
        self.size = 3
        self.index = 1
        self.value = 4
        self.array = Array(self.size)

    def test_length(self):
        assert len(self.array) == 3

    def test_clear(self):
        """after the array is created, all elements value should be set
            to None
        """
        array = Array(self.size)
        for i in range(len(array)):
            assert self.array._elements[i] == None

    def test_setItem(self):
        array = Array(self.size)
        array[self.index] = self.value
        assert array[self.index] == self.value

    def test_getItem(self):
        array = Array(self.size)
        array[self.index] = self.value
        assert array[self.index] == self.value

    def test_iterator(self):
        array = Array(5)
        val = 0
        for i in range(len(array)):
            array[i] = val
            val += 1
        idx = 0
        for e in array:
            array[idx] = idx + 1
            idx += 1

        assert array[1] == 2


class TestArray2d(unittest.TestCase):
    def setUp(self):
        self.nrows = 5
        self.ncols = 5
        self.array2d = Array2D(self.nrows, self.ncols)

    def test_setAndGetItem(self):
        colIdx = 0
        rowIdx = 0
        self.array2d[rowIdx, colIdx] = 2
        assert self.array2d[rowIdx, colIdx] == 2

    def test_clear(self):
        rowIdx = 0
        colIdx = 4
        assert self.array2d[rowIdx, colIdx] == None

        self.array2d.clear(0)
        assert self.array2d[rowIdx, colIdx] == 0

    def test_propertNColsAndRows(self):
        assert self.array2d.nCols == 5
        assert self.array2d.nRows == 5
