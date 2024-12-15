from array import Array
from linked_list import LinkedList
from stack import StackArray, StackLinkedList


def test_linked_list():
    print("Creating a linked list...")
    ll = LinkedList()

    # test 1: insert at the beginning
    # insert 10 and 5 at the beginning
    ll.insert_at_beginning(10)  # [10]
    ll.insert_at_beginning(5)  # [5 -> 10]
    ll.display()  # expected: 5 -> 10 -> None

    # test 2: insert at the end
    # insert 20 and 25 at the end of the list
    ll.insert_at_end(20)  # [5 -> 10 -> 20]
    ll.insert_at_end(25)  # [5 -> 10 -> 20 -> 25]
    ll.display()  # expected: 5 -> 10 -> 20 -> 25 -> None

    # test 3: insert at specific positions
    # insert 15 at position 2 and 30 at position 5
    ll.insert_at_position(15, 2)  # [5 -> 10 -> 15 -> 20 -> 25]
    ll.insert_at_position(30, 5)  # [5 -> 10 -> 15 -> 20 -> 25 -> 30]
    ll.display()  # expected: 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> None

    # test 4: insert at position 0 (beginning)
    # insert 1 at position 0 (beginning of the list)
    ll.insert_at_position(1, 0)  # [1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30]
    ll.display()  # expected: 1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> None

    # test 5: insert at an invalid position (negative)
    # attempt to insert at position -1, should raise an index error
    try:
        ll.insert_at_position(50, -1)
    except IndexError as e:
        print(e)  # expected: "Position must be a non-negative integer."

    # test 6: insert at an out-of-bound position
    # attempt to insert at position 10, should raise an index error
    try:
        ll.insert_at_position(40, 10)  # invalid: current length = 7
    except IndexError as e:
        print(e)  # expected: "Position out of bound"

    # test 7: insert into an empty list
    # create a new empty list and insert 100 at position 0
    empty_list = LinkedList()
    empty_list.insert_at_position(100, 0)  # [100]
    empty_list.display()  # expected: 100 -> None

    # test 8: insert at the last position
    # insert 35 at the last position (index 7)
    ll.insert_at_position(35, 7)  # [1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35]
    ll.display()  # expected: 1 -> 5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> None

    print("\nAll tests completed!")


def static_array_test():
    print("Testing static array...")
    arr = Array(5)  # create a static array of size 5

    # test inserting elements
    arr.insert(1, 0)
    arr.insert(2, 1)
    arr.insert(3, 2)
    arr.insert(4, 3)
    arr.insert(5)  # insert at the end
    arr.display()  # expected: 1 2 3 4 5

    # test overflow
    # attempt to insert 6 in a full array, should raise an overflow error
    try:
        arr.insert(6)
    except OverflowError as e:
        print(e)  # expected: "Array is full"

    # test deletion
    # delete the element at index 3 (value 4)
    arr.delete(3)  # deletes element at index 3
    arr.display()  # expected: 1 2 3 5 None

    # test insertion at a specific index
    # insert 6 at index 3
    arr.insert(6, 3)
    arr.display()  # expected: 1 2 3 6 5

    # test searching
    # search for 6 (should return index 3)
    print(arr.search(6))  # expected: 3
    # search for 4 (not found)
    print(arr.search(4))  # expected: "'4' not found"

    # test updating
    # update index 3 to value 7
    arr.update(3, 7)
    print(arr.search(7))  # expected: 3
    arr.display()  # expected: 1 2 3 7 5

    # test getting elements
    # get the element at index 3
    print(arr.get(3))  # expected: 7
    # attempt to get the element at index 5, should raise an index error
    try:
        print(arr.get(5))
    except IndexError as e:
        print(e)  # expected: "Index out of bound"

    print("Static array test completed.\n")


def dynamic_array_test():
    print("Testing dynamic array...")
    arr = Array()  # create a dynamic array

    # test inserting elements
    arr.insert(1, 0)
    arr.insert(2, 1)
    arr.insert(3, 2)
    arr.insert(4, 3)
    arr.insert(5)  # insert at the end
    arr.display()  # expected: 1 2 3 4 5

    # test deletion
    # delete the element at index 3 (value 4)
    arr.delete(3)
    arr.display()  # expected: 1 2 3 5

    # test insertion at a specific index
    # insert 6 at index 3
    arr.insert(6, 3)
    arr.display()  # expected: 1 2 3 6 5

    # test searching
    # search for 6 (should return index 3)
    print(arr.search(6))  # expected: 3
    # search for 4 (not found)
    print(arr.search(4))  # expected: "'4' not found"

    # test updating
    # update index 3 to value 7
    arr.update(3, 7)
    print(arr.search(7))  # expected: 3
    arr.display()  # expected: 1 2 3 7 5

    # test getting elements
    # get the element at index 3
    print(arr.get(3))  # expected: 7
    # get the element at index 4
    print(arr.get(4))  # expected: 5
    # attempt to get the element at index 6, should raise an index error
    try:
        print(arr.get(6))
    except IndexError as e:
        print(e)  # expected: "Index out of bound"

    # test adding additional elements
    # insert 99 and 100 at the end
    arr.insert(99)
    arr.insert(100)
    arr.display()  # expected: 1 2 3 7 5 99 100

    # insert 101 at index 6
    arr.insert(101, 6)
    arr.display()  # expected: 1 2 3 7 5 99 101 100
    print("Dynamic array test completed.\n")


def test_stack_array():
    print("Testing StackArray...")

    # test LIFO
    print("\nTest LIFO:")
    stack = StackArray(kind="LIFO")
    # import ipdb; ipdb.set_trace() c s n q
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # expected: Stack (lifo): 10 20 30
    print(stack.pop())  # expected: 30
    stack.display()  # expected: Stack (lifo): 10 20
    print("PEEK:", stack.peek())  # expected: 20

    # test FIFO
    print("\nTest FIFO:")
    stack = StackArray(kind="FIFO")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # expected: Stack (fifo): 30 20 10
    print(stack.pop())  # expected: 10
    stack.display()  # expected: Stack (fifo): 30 20
    print("PEEK:", stack.peek())  # expected: 20

    # test PRIORITY
    print("\nTest PRIORITY:")
    stack = StackArray(kind="PRIORITY")
    stack.push(50)
    stack.push(30)
    stack.push(40)
    stack.push(20)
    stack.display()  # expected: Stack (priority): 20 30 40 50
    print(stack.pop())  # expected: 20
    stack.display()  # expected: Stack (priority): 30 40 50
    print("PEEK:", stack.peek())  # expected: 30

    print("\nStackArray tests completed!")


def test_stack_linked_list():
    print("\nTesting StackLinkedList...")

    # test LIFO
    print("\nTest LIFO:")
    stack = StackLinkedList(kind="LIFO")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # expected: Stack (lifo): 30 -> 20 -> 10 -> None
    print(stack.pop())  # expected: 30
    stack.display()  # expected: Stack (lifo): 20 -> 10 -> None
    print("PEEK:", stack.peek())  # expected: 20

    # test FIFO
    print("\nTest FIFO:")
    stack = StackLinkedList(kind="FIFO")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # expected: Stack (fifo): 10 -> 20 -> 30 -> None
    print(stack.pop())  # expected: 10
    stack.display()  # expected: Stack (fifo): 20 -> 30 -> None
    print("PEEK:", stack.peek())  # expected: 20

    # test PRIORITY
    print("\nTest PRIORITY:")
    stack = StackLinkedList(kind="PRIORITY")
    stack.push(50)
    stack.push(30)
    stack.push(40)
    stack.push(20)
    stack.display()  # expected: Stack (priority): 20 -> 30 -> 40 -> 50 -> None
    print(stack.pop())  # expected: 20
    stack.display()  # expected: Stack (priority): 30 -> 40 -> 50 -> None
    print("PEEK:", stack.peek())  # expected: 30

    print("\nStackLinkedList tests completed!")


if __name__ == "__main__":
    # static_array_test()  # test static array
    # dynamic_array_test()  # test dynamic array
    # test_linked_list()  # test linked list
    test_stack_array()  # test stack array
    test_stack_linked_list()  # test stack linked list
