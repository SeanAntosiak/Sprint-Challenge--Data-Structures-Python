from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.current.next:
                new = ListNode(item,
                               prev=self.current,
                               next=self.current.next.next)

                self.current.next = new
                self.current = self.current.next
            else:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while len(list_buffer_contents) != self.storage.length:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# TESTS AND BAD CODE ###


# test = RingBuffer(5)
#
# test.append(1)
# test.append(2)
# test.append(3)
# test.append(4)
# test.append(5)
# test.append(2)
#
# test.current.value
#
# test.get()
#
# test.storage.length
#
# test.storage.head.next.value

# returned out of order
# def get(self):
#     # Note:  This is the only [] allowed
#     list_buffer_contents = []
#     current = self.current
#     while len(list_buffer_contents) != self.storage.length:
#         if current.prev:
#             current = current.prev
#             list_buffer_contents.append(current.value)
#         elif (current.prev is None) & (current.next is not None):
#             current = self.storage.tail
#             list_buffer_contents.append(current.value)
#         else:
#             list_buffer_contents.append(current.value)
#     return list_buffer_contents
