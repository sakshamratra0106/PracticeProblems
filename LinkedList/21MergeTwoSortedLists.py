# Importing Self Created LinkedList Implementation
# Linked List which has __init__, __str__, push(), detectLoop() : O(N), removeElements() : O(N)
from LinkedList import *

if __name__ == "__main__":

    # Creating LinkedList 1
    list1 = LinkedList()

    # Inserting Values to Linked List 1
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.push(5)
    list1.push(6)

    # Printing Values of Linked List 1
    print("Printing {} : {}".format(list1.__class__.__name__, list1))
