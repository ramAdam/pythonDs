import unittest
from data import rotArray


class TestRotationArrayData(unittest.TestCase):

    def testAndTestTopRow(self):
        for j in range(1, rotArray.nCols):
            assert rotArray[0, j] == 1

    def testAndTestRightColumn(self):
        for i in range(1, rotArray.nRows):
            assert rotArray[i, rotArray.nCols - 1] == 2

    def testAndTestBottomRow(self):
        for i in range(rotArray.nCols-2, -1, -1):
            assert rotArray[rotArray.nRows-1, i] == 3

    def testLeftColumn(self):
        for i in range(0, rotArray.nRows - 1):
            assert rotArray[i, 0] == 4
