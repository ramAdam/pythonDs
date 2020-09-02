from linalg import Matrix


def populateMatrix(matrix, data):
    for row in matrix:
        for i in range(len(row)):
            row[i] = data.pop()


ncols = 2
nrows = 3
matrix = Matrix(nrows, ncols)
data = [0, 1, 2, 3, 4, 5]
data.reverse()
populateMatrix(matrix, data)

other = Matrix(nrows, ncols)
otherData = [6, 7, 8, 9, 1, 0]
otherData.reverse()
populateMatrix(other, otherData)

result = Matrix(nrows, ncols)
resultData = [6, 8, 10, 12, 5, 5]
resultData.reverse()
populateMatrix(result, resultData)


subtractResult = Matrix(nrows, ncols)
subtractionData = [-6, -6, -6, -6, 3, 5]
subtractionData.reverse()
populateMatrix(subtractResult, subtractionData)

# spare matrix
spareMatrix = Matrix(nrows, ncols)

# scaled matrix result
scaledMatrix = Matrix(nrows, ncols)
scaledData = [0, 2, 4, 6, 8, 10]
scaledData.reverse()
populateMatrix(scaledMatrix, scaledData)
