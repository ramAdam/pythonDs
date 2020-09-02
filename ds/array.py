import ctypes
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


class Array:
    def __init__(self, size):
        """ Creates a one-dimensional array consisting of 
            size elements with each element initially
            set to None. size must be greater than zero"""
        self.size = size
        ArrayType = ctypes.py_object * self.size
        self._elements = ArrayType()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < self.size, "index out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < self.size, "index out of range"
        self._elements[index] = value

    def __iter__(self):
        return _ArrayIterator(self)

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value


class Array2D:
    def __init__(self, nrows, ncols):

        self._nRows = Array(nrows)
        for i in range(nrows):
            self._nRows[i] = Array(ncols)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "invalid array subscript"
        rowIdx, colIdx = ndxTuple
        assert rowIdx >= 0 and rowIdx < self.numRows(), "row index, out of range"
        assert colIdx >= 0 and colIdx < self.numCols(), "col index, out of range"
        return self._nRows[rowIdx][colIdx]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "invalid array subscript"
        rowIdx, colIdx = ndxTuple
        assert rowIdx >= 0 and rowIdx < self.numRows(), "row index, out of range"
        assert colIdx >= 0 and colIdx < self.numCols(), "col index, out of range"
        self._nRows[rowIdx][colIdx] = value

    def __iter__(self):
        return _ArrayIterator(self._nRows)

    def numRows(self):
        return len(self._nRows)

    def numCols(self):
        return len(self._nRows[0])

    def clear(self, value):
        for i in range(self.numRows()):
            assert self._nRows[i] is not None, "row on index {} is None".format(
                i)
            self._nRows[i].clear(value)

    def __repr__(self):
        l = []
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                l.append(str(self[i, j]))
        return "".join(l)
