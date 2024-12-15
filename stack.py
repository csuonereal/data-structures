from array import Array
from linked_list import Node, LinkedList
from abc import ABC, abstractmethod


class StackBase(ABC):
    """this class can't be instantiated, it is an abstract class"""

    def __init__(self, kind="LIFO"):
        self._data = None
        self.kind = kind.upper()
        if self.kind not in {"LIFO", "FIFO", "PRIORITY"}:
            raise ValueError("Invalid stack kind. Choose 'LIFO', 'FIFO', or 'PRIORITY'.")

    def push(self, value):
        if self.kind == "LIFO":
            self._push_lifo(value)
        elif self.kind == "FIFO":
            self._push_fifo(value)
        elif self.kind == "PRIORITY":
            self._push_priority(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self._pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._peek_top()

    def is_empty(self):
        return self._is_empty()

    def display(self):
        return self._display()

    @abstractmethod
    def _push_lifo(self, value):
        pass

    @abstractmethod
    def _push_fifo(self, value):
        pass

    @abstractmethod
    def _push_priority(self, value):
        pass

    @abstractmethod
    def _pop(self):
        pass

    @abstractmethod
    def _peek_top(self):
        pass

    @abstractmethod
    def _is_empty(self):
        pass

    @abstractmethod
    def _display(self):
        pass


class StackArray(StackBase):
    """
    abstract base class for stack implementations.

    this class provides a common interface for all stack types (LIFO, FIFO, PRIORITY)
    and enforces the implementation of required methods in child classes.
    """

    def __init__(self, kind="LIFO"):
        super().__init__(kind)
        self._data = Array()

    def _push_lifo(self, value):
        # lifo (last in, first out):
        # insert the new element at the beginning (index=0)
        # so the last pushed element is always at the front
        self._data.insert(value=value, index=0)

    def _push_fifo(self, value):
        # fifo (first in, first out):
        # insert the new element at the end (index=self._data.length)
        # so the first inserted element remains at the front
        self._data.insert(value=value, index=self._data.length)

    def _push_priority(self, value):
        # priority: insert the element in sorted order based on its value
        # lower values have higher priority and are removed first
        if self._data.is_empty():
            self._data.insert(value=value, index=0)
            return
        for i in range(self._data.length):
            if value < self._data.get(i):
                self._data.insert(value=value, index=i)
                return
        self._data.insert(value=value,
                          index=self._data.length)  # if the value is greater than all elements, add it to the end

    def _pop(self):
        # regardless of the stack type (lifo, fifo, priority), the removal operation is always the same
        # this is because:
        # - for lifo, we insert new elements at the end, and the last element becomes the first in the stack's logic
        # - for fifo, we insert new elements at the beginning, so the first-in element is already at the front
        # - for priority, elements are inserted in sorted order, and the lowest value is always at the front
        # therefore, for all types, popping simply means removing the first element (index 0)
        if self._data.is_empty():
            raise IndexError("Stack is empty")
        value = self._data.get(0)
        self._data.delete(0)
        return value

    def _peek_top(self):
        if self._data.is_empty():
            raise IndexError("Stack is empty")
        return self._data.get(0)

    def _is_empty(self):
        return self._data.is_empty()

    def _display(self):
        print(f"Stack ({self.kind.lower()}):", end=" ")
        self._data.display()


class StackLinkedList(StackBase):
    """for this class, we will use our LinkedList class to store the stack elements"""

    def __init__(self, kind="LIFO"):
        super().__init__(kind)
        self._data = LinkedList()

    def _push_lifo(self, value):
        # lifo (last in, first out): add the element to the beginning of the linked list
        # the last element added will be the first one to be removed
        self._data.insert_at_beginning(value)

    def _push_fifo(self, value):
        # fifo (first in, first out): add the element to the end of the linked list
        # the first element added will be the first one to be removed
        self._data.insert_at_end(value)

    def _push_priority(self, value):
        # priority: insert the element in sorted order based on its value
        # lower values have higher priority and are removed first
        if self._data.is_empty():
            self._data.insert_at_beginning(value)  # if the list is empty, insert at the beginning and
            return
        current = self._data.head
        position = 0
        while current and current.data < value:
            # find the position to insert the new node
            # if the current node's value is less than the new value, move to the next node
            current = current.next
            position += 1
        self._data.insert_at_position(value, position)

    # [10] -> [20] -> [30] -> None
    # lifo: push 40: [40] -> [10] -> [20] -> [30] -> None
    # fifo: push 40: [10] -> [20] -> [30] -> [40] -> None
    # lifo: pop: [10] -> [20] -> [30] -> None

    def _pop(self):
        # lifo (last in, first out): remove and return the first element of the linked list
        # in a linked list, the last element added is always at the head when using lifo
        # this is because we insert new elements at the beginning (head)
        if self._data.is_empty():
            raise IndexError("Stack is empty")
        value = self._data.head.data
        self._data.head = self._data.head.next
        return value

    def _peek_top(self):
        # return the first element for fifo or priority stacks
        # return the first element for lifo since the last added is always at the head
        if self._data.is_empty():
            raise IndexError("Stack is empty")
        return self._data.head.data

    def _is_empty(self):
        return self._data.is_empty()

    def _display(self):
        print(f"Stack ({self.kind.lower()}):", end=" ")
        self._data.display()
