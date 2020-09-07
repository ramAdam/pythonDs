import unittest
from data import matrix, result, other, transMatrix


class TestPopulateMatrix(unittest.TestCase):
    def testAddResultMatrix(self):
        resultTestData = [6, 8, 10, 12, 5, 5]
        resultTestData.reverse()
        self._assertPopulatedMatrix(result, resultTestData)

    def testPopulatedMatrix(self):
        data = [0, 1, 2, 3, 4, 5]
        data.reverse()
        self._assertPopulatedMatrix(matrix, data)

    def testOtherPopulatedMatrix(self):
        testData = [6, 7, 8, 9, 1, 0]
        testData.reverse()
        self._assertPopulatedMatrix(other, testData)

    def testTransposedPopulateMatrix(self):
        transTestData = [0, 2, 4, 1, 3, 5]
        transTestData.reverse()
        assert transMatrix[0, 1] == 2
        assert transMatrix[0, 2] == 4
        assert transMatrix[1, 2] == 5
        self._assertPopulatedMatrix(transMatrix, transTestData)

    def _assertPopulatedMatrix(self, matrix, data):
        for row in matrix:
            for i in range(len(row)):
                assert row[i] == data.pop()
