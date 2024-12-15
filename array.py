class Array:  # dynamic and static array
    def __init__(self, size=None):
        self.length = 0  # number of elements in the array
        self.size = size
        self.array = [0] * self.size if self.size is not None else []

    def insert(self, value, index=None):

        if index is not None and self.is_index_out_of_bound(index):
            raise IndexError("Index out of bound")

        if self.size is not None and self.length >= self.size:
            raise OverflowError("Array is full")

        if index is None:
            index = self.length

        if self.size:  # static array insertion
            for i in range(self.length, index, -1):
                # example: array is [1, 2, 3, 4, 5], and we want to insert a new value at index 2
                # to make space for the new value:
                # - start shifting elements from the last element (index 4) to the target index (index 2)
                # - move each element one position to the right
                # for instance:
                #   - element at index 4 will move to index 5
                #   - element at index 3 will move to index 4, and so on
                self.array[i] = self.array[i - 1]
            self.array[index] = value
        else:  # dynamic array insertion
            self.array.insert(index, value)

        self.length += 1

    def get(self, index):
        if self.is_index_out_of_bound(index):
            raise IndexError("Index out of bound")
        return self.array[index]

    def delete(self, index):
        if self.is_index_out_of_bound(index):
            raise IndexError("Index out of bound")
        for i in range(index, self.length - 1):
            # example: array is [1, 2, 3, 4, 5], and we want to delete the element at index 2 (value 3)
            # to fill the gap left by the deleted element:
            # - start shifting elements from index 3 to the left
            # - move each element one position to the left
            # for instance:
            #   - element at index 3 will move to index 2
            #   - element at index 4 will move to index 3, and so on
            # the last element will remain unchanged or can be set to none if using a static array
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None  # clear the last element for static arrays to avoid duplicates
        self.length -= 1

    def search(self, value):
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return f"'{value}' not found"

    def update(self, index, value):
        if self.is_index_out_of_bound(index):
            raise IndexError("Index out of bound")
        self.array[index] = value

    def display(self):
        for i in range(self.length):
            print(self.array[i], end=" ")
        print()

    def display_at_index(self, index):
        if self.is_index_out_of_bound(index):
            raise IndexError("Index out of bound")
        print(self.array[index])

    def is_empty(self):
        return self.length == 0

    def is_index_out_of_bound(self, index):
        return index < 0 or index > self.length
