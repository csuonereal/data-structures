class Node:
    def __init__(self, data):
        self.data = data  # node's value
        self.next = None  # the pointer initially points to nothing


class LinkedList:
    def __init__(self):
        # [A] -> None
        self.head = None  # the linked list is initially empty

    def insert_at_beginning(self, data):
        # [B] -> None
        new_node = Node(data)
        # [B] -> [A] -> None
        new_node.next = self.head
        # self.head = [B] now the head points to the new node
        # self.head -> [B] -> [A] -> None
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        # iterate through the linked list to find the last node
        while last.next is not None:
            # move to the next node
            last = last.next
        # make the last node's next point to the new node
        last.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position must be a non-negative integer.")
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < position - 1:  # find the node before the target position
            current = current.next
            count += 1

        # if current is None:  # we reached the end of the list
        #     self.insert_at_end(data)
        # above scenario won't be happen because we stopped iteration before the target position so
        # even last item intended to be target position, current will be one node before the target position
        if current is None:
            raise IndexError("Position out of bound")
        else:
            # A -> B -> C -> None
            # insert a new node X at position 2, between B and C.
            # current = B
            # current.next = C
            # new_node.next = C
            # current.next = X
            new_node.next = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None
