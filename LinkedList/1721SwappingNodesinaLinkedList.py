# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from LinkedList import Node, LinkedList


class Solution:
    def swapNodes(self, head: Optional[Node], k: int) -> Optional[Node]:

        # Return head of its None
        if head is None:
            return head

        # Prepare a equivalent array of list
        inputList = []
        temp = head
        while temp:
            inputList.append(temp.value)
            temp = temp.next

        # Swap values
        temp = inputList[k - 1]
        inputList[k - 1] = inputList[-k]
        inputList[-k] = temp

        # Re-create Linked List
        temp = head
        index = 0

        while temp:
            temp.value = inputList[index]
            index += 1
            temp = temp.next

        return head

    def swapNodes1(self, head: Optional[Node], k: int) -> Optional[Node]:

        # Return head of its None
        if head is None:
            return head

        l = r = head

        # Find the left element
        for _ in range(k - 1):
            l = l.next

        # Find the right element
        tail = l
        while tail.next:
            r, tail = r.next, tail.next

        # Swap
        l.value, r.value = r.value, l.value

        return head


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
    k = 2
    # Printing Values of Linked List 1
    Solution().swapNodes(list1.head, k)
    print("1. {} after swapping {}th element will be {}.".format(
        list1.__class__.__name__, k, list1
    ))
