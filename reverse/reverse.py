class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)

    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    current = self.head
    while (current) and (current.next_node):
        next = current.next_node
        current.next_node = next.next_node
        if current.next_node:
            self.add_to_head(current.next_node.value)
        else:
            reversing = 0

# --- tests ---
# 
# ll = LinkedList()
# ll.add_to_head(1)
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.add_to_head(4)
# ll.add_to_head(5)
# ll.head.value
# ll.reverse_list()
# ll.head.value
# ll.head.next_node.value
# ll.head.next_node.next_node.value
# ll.head.next_node.next_node.next_node.value
# ll.head.next_node.next_node.next_node.next_node.value

#  weird errors
# current = self.head
# if current:
#     while current.next_node:
#         next = current.next_node
#         current.next_node = next.next_node
#         if current.next_node:
#             self.add_to_head(current.next_node.value)
