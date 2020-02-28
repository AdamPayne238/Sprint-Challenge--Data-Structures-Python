from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # The append method adds elements to the buffer.
    def append(self, item):
        # if capacity is greater than storage length
        if self.capacity > self.storage.length:
            # add item to tail
            self.storage.add_to_tail(item)

        # if capacity is equal to storage length
        if self.capacity == self.storage.length:
            remove = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if remove == self.current:
                self.current = self.storage.tail

    # The get method, which is provided, returns all of the elements in the buffer in a
    # list in their given order. It should not return any None values in the list even
    # if they are present in the ring buffer.
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.current
        list_buffer_contents.append(current_node.value)

        # if start is not none
        if current_node:
            next_node = current_node.next
        else:
            next_node = self.storage.head

        while next_node is not current_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
