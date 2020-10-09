import unittest
import pdb
from ds import Bag
import hypothesis.strategies as st
from hypothesis import given
from hypothesis.stateful import GenericStateMachine


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def testAdd(self):
        self.bag.add(1)
        assert len(self.bag) == 1
        assert self.bag.head.item == 1

        self.bag.add(3)
        assert len(self.bag) == 2
        assert self.bag.head.item == 3
        assert self.bag.head.next.item == 1

    @given(x=st.integers())
    def testRemove(self, x):
        bag = Bag()
        bag.add(1)
        assert len(bag) == 1
        bag.remove(1)
        assert len(bag) == 0
        bag.add(2)
        bag.add(1)
        assert len(bag) == 2
        bag.remove(2)
        bag.remove(1)
        assert len(bag) == 0
        bag.remove(1)
        assert len(bag) == 0
        bag.remove(3)
        assert len(bag) == 0

        bag.add(2)
        bag.add(1)
        bag.remove(1)

        assert len(bag) == 1
        assert bag.head.item == 2
        assert not bag.head.next

    def testContains(self):
        bag = Bag()
        bag.add(2)

        assert 2 in bag
        assert 1 not in bag

    def testBagIterator(self):
        bag = Bag()
        bag.add(1)
        bag.add(2)
        bag.add(3)

        bagIter = iter(bag)
        assert next(bagIter).item == 3
        assert next(bagIter).item == 2
        assert next(bagIter).item == 1
        self.assertRaises(StopIteration, bagIter.__next__)


class TestStatefulBag(unittest.TestCase):

    def setUp(self):
        """
        docstring
        """
        pass

    def testAddRemove(self):
        bag = Bag()

        bag.add(0)
        bag.add(0)
        pdb.set_trace()
        bag.remove(0)
