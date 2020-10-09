from trace import Trace
from unittest.case import expectedFailure
from ds.bag import Bag
import unittest
from ds import bag
import trace
import pdb


class TestTrace(unittest.TestCase):
    def setUp(self) -> None:
        self.bag = Bag()
        self.trace = trace.Trace(trace=0, count=1)

    def testAddBagLoc(self):
        """
        count number of lines executed
        """
        self.trace.runfunc(self.bag.add, 1)
        loc = sum(getattr(self.trace, 'counts').values())
        self.assertEqual(loc, 5)

    def testRemoveBagLoc(self):
        """
        count number of line executed while executiy bag.remove()
        """
        self.trace.runfunc(self.bag.add, 2)
        self.trace.runfunc(self.bag.add, 1)
        self.trace.runfunc(self.bag.remove, 2)
        r = self.trace.results()
        r.write_results(show_missing=False, coverdir=".")
        loc = sum(getattr(self.trace, 'counts').values())
        expectedLoc = 39
        self.assertEqual(loc, expectedLoc)

    def tearDown(self):
        """
        cleans up all refrences in setUp
        """
        del self.trace
        del self.bag
