from typing import Optional
from LinkedList import *


def deleteDuplicates(head: Optional[Node]) -> Optional[Node]:
    current = head
    while current and current.next:
        # print("--",current.val,"--",current.next.val)
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head


class Solution:
    pass


if __name__ == "__main__":
    # Creating a Linked List
    list1 = LinkedList()
    list1.push(1)
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(4)
    list1.push(5)
    list1.push(5)

    print("The {} is : {}".format(
        list1.__class__.__name__, list1
    ))

    print(" After removing duplicates it is : {}".format(
        LinkedList(deleteDuplicates(list1.head))
    ))

    # poping Values out
    print("\n Poped top value {} from the above list. After Pop list will be : {}".format(
        list1.pop(), list1
    ))
