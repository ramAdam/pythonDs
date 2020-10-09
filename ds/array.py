import ctypes
from typing import Generic, TypeVar
import pdb


class _ArrayIterator:
    def __init__(self, theArray):
        self._array = theArray
        self._curIndex = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curIndex < len(self._array):
            entry = self._array[self._curIndex]
            self._curIndex += 1
            return entry
        else:
            raise StopIteration


T = TypeVar('T')


class Array(Generic[T]):
    def __init__(self, size):
        """ Creates a one-dimensional array consisting of
            size elements with each element initially
            set to None. size must be greater than zero"""
        assert size > 0, "size must be greater than zero"
        self.size = size
        ArrayType = ctypes.py_object * self.size
        self._elements = ArrayType()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "index out of range"
        return self._elements[index]

    def __setitem__(self, index, value: T):
        assert index >= 0 and index < self.size, "index out of range"
        self._elements[index] = value

    def __iter__(self):
        return _ArrayIterator(self)

    def __repr__(self):
        l = []
        l.append('[')
        for i in range(len(self)):
            l.append(str(self[i]) + ", ")
        l.append("]\n")

        return "".join(l)

    def clear(self, value: T):
        for i in range(len(self)):
            self._elements[i] = value


class Array2D:
    def __init__(self, nrows, ncols):

        self._rows = Array(nrows)
        assert ncols > 0, "number of cols must be greater than 0"
        for i in range(nrows):
            self._rows[i] = Array(ncols)
        self._nRows = len(self._rows)
        self._nCols = len(self._rows[0])

    @property
    def nRows(self):
        return self._nRows

    @property
    def nCols(self):
        return self._nCols

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "invalid array subscript"
        rowIdx, colIdx = ndxTuple
        assert rowIdx >= 0 and rowIdx < self.numRows(), "row index, out of range"
        assert colIdx >= 0 and colIdx < self.numCols(), "col index, out of range"
        return self._rows[rowIdx][colIdx]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "invalid array subscript"
        rowIdx, colIdx = ndxTuple
        assert rowIdx >= 0 and rowIdx < self.numRows(), "row index, out of range"
        assert colIdx >= 0 and colIdx < self.numCols(), "col index, out of range"
        self._rows[rowIdx][colIdx] = value

    def __iter__(self):
        return _ArrayIterator(self._rows)

    def numRows(self):
        return len(self._rows)

    def numCols(self):
        return len(self._rows[0])

    def clear(self, value):
        for i in range(self.numRows()):
            assert self._rows[i] is not None, "row on index {} is None".format(
                i)
            self._rows[i].clear(value)

    def __repr__(self):
        l = []
        for i in range(self.numRows()):
            l.append("[ ")
            for j in range(self.numCols()):
                l.append(str(self[i, j]) + ' ')
            l.append(']\n')
        return "".join(l)
