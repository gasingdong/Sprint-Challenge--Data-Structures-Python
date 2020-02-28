from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) >= self.capacity:
            if not self.current:
                self.current = self.storage.head
            self.current.value = item
            self.current = self.current.next \
                if self.current.next else self.storage.head
        else:
            self.storage.add_to_tail(item)

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None for index in range(0, capacity)]

    def append(self, item):
        self.storage[self.current] = item
        self.current = self.current + 1 \
            if self.current < self.capacity - 1 else 0

    def get(self):
        return [value for value in self.storage if value]
