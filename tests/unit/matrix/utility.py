def assertPopulatedMatrix(matrix, data):
    for row in matrix:
        for i in range(len(row)):
            assert row[i] == data.pop()
