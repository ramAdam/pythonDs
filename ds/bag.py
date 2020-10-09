from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule
import hypothesis.strategies as st


class _BagIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if not self.current:
            raise StopIteration
        next = self.current
        self.current = self.current.next
        return next

    def __iter__(self):
        return self


class _BagListNode:
    def __init__(self, item=None):
        self.item = item
        self.nxt = None

    @property
    def next(self):
        return self.nxt

    @next.setter
    def next(self, node):
        self.nxt = node


class Bag:

    def __init__(self):
        self.head = None
        self._size = 0

    items = Bundle("items")

    def add(self, item):
        """prepends a node to the head"""
        size_before = self._size
        if self._size == 0:
            self.head = _BagListNode(item)
            self._size += 1
        else:
            tmp = self.head
            self.head = _BagListNode(item)
            self.head.next = tmp
            self._size += 1

        assert self.head.item == item
        assert self._size > size_before

    def remove(self, item):
        """finds and removes a node from linked list"""
        prev = None
        if self._size == 0:
            return
        size_before = self._size
        for e in self:
            try:
                if e.item == item:
                    prev.next = e.next
                    self._size -= 1
                    assert item not in self and self._size < size_before
                    return
                prev = e
            except AttributeError:
                self.head = self.head.next
                self._size -= 1
                assert item not in self and self._size < size_before
                return

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self.head)

    def __contains__(self, target):
        for e in self:
            if e.item == target:
                return True
        return False

    def __repr__(self):
        l = []
        l.append('[ ')
        for e in self:
            l.append(str(e.item))
            l.append(' ,')
        l.pop()
        l.append(' ]')
        return "".join(l)
