from ds import Array2D


def _populateTopRow(array: Array2D):
    top = [1] * (array.nCols - 1)
    assert len(top) == 5

    for j in range(1, array.nCols):
        array[0, j] = top[j - 1]


def _populateRightColumn(array: Array2D):
    right = [2] * array.nRows
    assert len(right) == 10
    for i in range(1, array.nRows):
        array[i, array.nCols - 1] = right[i]


def _populateBottomRow(array: Array2D):
    bottom = [3] * array.nCols

    for i in range(array.nCols-2, -1, -1):
        array[array.nRows-1, i] = bottom[i]


def _populateLeftColumn(array: Array2D):
    left = [4] * array.nRows

    for i in range(0, array.nRows - 1):
        array[i, 0] = left[i]


def initRotArray(nCols, nRows):
    array = Array2D(nRows, nCols)
    array.clear(0)
    _populateTopRow(array)
    _populateRightColumn(array)
    _populateBottomRow(array)
    _populateLeftColumn(array)

    return array


rotArray = initRotArray(6, 10)
