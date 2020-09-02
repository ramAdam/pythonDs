from ds.array import Array2D


class _MatrixIterator:
    def __init__(self, matrix):
        assert isinstance(
            matrix, (Array2D)), "matrix is not instance of array2d"
        self._array2d = matrix
        self.nrows = self._array2d.numRows()
        self.ncols = self._array2d.numCols()
        self.i = 0
        self.j = 0

    def _incrementIndices(self):
        pass

    def __next__(self):
        try:
            val = self._array2d[self.i, self.j]
            self._incrementIndices()
            return val
        except IndexError as error:
            print(error.__cause__)

    def __iter__(self):
        return self


class Matrix(Array2D):

    def __init__(self, nrows, ncols):
        super(Matrix, self).__init__(nrows, ncols)
        self.clear(0)

    def __add__(self, other):
        assert self.colsRowsEqual(
            other), "number of rows or cols are not equal"
        result = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __sub__(self, other):
        assert self.colsRowsEqual(
            other), "number of rows or cols are not equal"
        result = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __mul__(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self[i, j] = self[i, j] * scalar

    def __eq__(self, other):
        if not self.colsRowsEqual(other):
            return False
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if not self[i, j] == other[i, j]:
                    return False
        return True

    def scaleBy(self, scalar):
        pass

    def transpose(self):
        pass

    def colsRowsEqual(self, other):
        assert isinstance(
            other, (Matrix)), "other is not a instance of matrix"
        return self.numRows() == other.numRows() and self.numCols() == other.numCols()
