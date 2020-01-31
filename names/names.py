import time
from binary_search_tree import BinarySearchTree as bst
from doubly_linked_list import DoublyLinkedList as dll

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

n1 = bst(names_1[0])
for name in names_1[1:]:
    n1.insert(name)

n2 = dll()
for name in names_2:
    n2.add_to_tail(name)

duplicates = dll()

current = n2.head
while current:
    if n1.contains(current.value):
        duplicates.add_to_tail(current.value)
        current = current.next
    else:
        current = current.next

end_time = time.time()
print (f"{duplicates.length} duplicates")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?


# ------- Original code ------ O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
