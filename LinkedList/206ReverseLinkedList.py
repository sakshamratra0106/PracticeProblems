from typing import Optional
from LinkedList import *


def reverseList(head: Optional[Node]) -> Optional[Node]:
    temp = head

    reversedHead = None

    while temp:
        # Pushing New element to ReversedHead
        newNode = Node(temp.value)
        newNode.next = reversedHead
        reversedHead = newNode

        # Traversing Original List Head
        temp = temp.next

    return reversedHead


class Solution:
    pass


if __name__ == "__main__":

    # Creating a List
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(3)
    list1.push(2)
    list1.push(1)

    print("1. Give a Linked List {}, revered linked list would be {}".format(
        list1, LinkedList(reverseList(list1.head))
    ))