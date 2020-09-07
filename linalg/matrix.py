from ds.array import Array2D


class _MatrixIterator:
    def __init__(self, matrix):
        assert isinstance(
            matrix, (Array2D)), "matrix is not instance of array2d"
        self._array2d = matrix
        self.nrows = self._array2d.nRows
        self.ncols = self._array2d.nCols
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
        result = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                result[i, j] = self[i, j] + other[i, j]
        return result

    def __sub__(self, other):
        assert self.colsRowsEqual(
            other), "number of rows or cols are not equal"
        result = Matrix(self.nRows, self.nCols)
        for i in range(self.nRows):
            for j in range(self.nCols):
                result[i, j] = self[i, j] - other[i, j]
        return result

    def __mul__(self, scalar):
        for i in range(self.nRows):
            for j in range(self.nCols):
                self[i, j] = self[i, j] * scalar

    def __eq__(self, other):
        if not self.colsRowsEqual(other):
            return False
        for i in range(self.nRows):
            for j in range(self.nCols):
                if not self[i, j] == other[i, j]:
                    return False
        return True

    def transpose(self):
        """retuns a new matrix that is tranpose of this matrix"""
        t = Matrix(self.nCols, self.nRows)
        for i in range(t.nRows):
            for j in range(self.nRows):
                t[i, j] = self[j, i]

        return t

    def colsRowsEqual(self, other):
        assert isinstance(
            other, (Matrix)), "other is not a instance of matrix"
        return self.nRows == other.nRows and self.nCols == other.nCols
