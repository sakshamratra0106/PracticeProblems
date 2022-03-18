# Importing Self Created LinkedList Implementation
# Linked List which has __init__, __str__, push(), detectLoop() : O(N), removeElements() : O(N)
from LinkedList import *


def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:

    # Time Complexity:  Since we are traversing through the two lists fully.
    # So, the time complexity is O(m+n) where m and n are the lengths of the two lists to be merged.

    # third Method in below link
    # https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/

    # base case
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    # pattern
    elif list1.value < list2.value:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list2.next, list1)
        return list2


if __name__ == "__main__":
    # Creating LinkedList 1
    list11 = LinkedList()

    # Inserting Values to Linked List 1
    list11.push(6)
    list11.push(5)
    list11.push(4)
    list11.push(3)
    list11.push(2)
    list11.push(1)

    # Printing Values of Linked List 1
    print("Printing {} : {}".format(list11.__class__.__name__, list11))

    # Creating LinkedList 2
    list12 = LinkedList()

    # Inserting Values to Linked List 2
    list12.push(6)
    list12.push(5)
    list12.push(4)
    list12.push(3)
    list12.push(2)
    list12.push(1)

    # Printing Values of Linked List 2
    print("Printing {} : {}".format(list12.__class__.__name__, list12))

    # Merge two Linked List
    print("Printing two {} : \n First is {} \n Second is {}".format(
        list12.__class__.__name__,
        list11,
        list12,
        )
    )

    print("\n Merged Linked List is {}".format(
        LinkedList(mergeTwoLists(list11.head, list12.head))
        )
    )
