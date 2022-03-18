# Importing Self Created LinkedList Implementation
# Linked List which has __init__, __str__, push(), detectLoop() : O(N), removeElements() : O(N)
from LinkedList import *


def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    # base case
    temp1 = list1
    temp2 = list2


    if temp1 is None:
        return temp2
    elif temp2 is None:
        return temp1
    # pattern
    elif temp1.value < temp2.value:
        temp1.next = mergeTwoLists(temp1.next, temp2)
        return temp1
    else:
        temp2.next = mergeTwoLists(temp2.next, temp1)
        return temp2


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
