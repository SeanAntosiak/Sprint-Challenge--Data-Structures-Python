from doubly_linked_list import DoublyLinkedList as dll
from doubly_linked_list import ListNode


class Queue:
    def __init__(self):
        self.size = 0
        self.list = dll()

    def enqueue(self, value):
        self.list.add_to_head(value)
        self.size = self.list.length

    def dequeue(self):
        if self.size == 0:
            return(None)
        else:
            val = self.list.remove_from_tail()
            self.size = self.list.length
            return(val)

    def len(self):
        return(self.size)
