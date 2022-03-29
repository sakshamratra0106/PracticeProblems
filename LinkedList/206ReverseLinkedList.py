from typing import Optional
from LinkedList import *


def reverseList(head: Optional[Node]) -> Optional[Node]:
    """

    :param head:
    :return:

    Reverses the LinkedList
    with Time complexity O(N) and O(N) space complexity

    """
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


def reverseList1(head: Optional[Node]) -> Optional[Node]:
    """

    :param head: Pointing to the head of the linked list
    :return: head pointed to linked list in reversed order of originally provided

    Time Complexity : O(N)
    Space Complexity : O(1)

    """

    reversedList = None

    while head:
        temp = head
        head = head.next

        # inserting the top of the LL to reversedList
        temp.next = reversedList
        reversedList = temp

        # print(reversesList)
        # print(temp.value)

    return reversedList


def reverseList2(head: Optional[Node]) -> Optional[Node]:
    """
    :param head:
    :return:

    Recursive Function
    Time Complexity : O(N)
    Space Complexity : O(1)

    """

    # If head is empty or has reached the list end
    if head is None or head.next is None:
        return head

    # Reverse the rest list
    rest = reverseList2(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest


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

    # Creating a List
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(3)
    list1.push(2)
    list1.push(1)

    # Was trying to keep the initial state of the Linked List
    # in some temp LL but the function "reverseList1"
    # changes the internal structure of the LL hence the prior is distorted
    # Hence commenting the code out
    # listTemp = list1

    print("2. Give a Linked List {}, revered linked list would be {}".format(
        "Head-->1-->2-->3-->4-->5-->None", LinkedList(reverseList1(list1.head))
    ))

    # Creating a List
    list1 = LinkedList()
    list1.push(5)
    list1.push(4)
    list1.push(3)
    list1.push(2)
    list1.push(1)

    print("3. Give a Linked List {}, revered linked list would be {}".format(
        "Head-->1-->2-->3-->4-->5-->None", LinkedList(reverseList2(list1.head))
    ))