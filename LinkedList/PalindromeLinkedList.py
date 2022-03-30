# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from LinkedList import *


class Solution:
    def isPalindrome(self, head: Optional[Node]) -> bool:
        """

        :param head:
        :return:
        """

        # If list is empty
        if head is None:
            return True

        # Find middle of the list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = reverseList(slow.next)

        # check if palindrome
        current = head
        temp = slow.next
        while temp:
            if temp.value != current.value:
                return False
            temp = temp.next
            current = current.next

        # All checks have passed
        return True


if __name__ == "__main__":
    # Creating a List
    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    # list1.push(3)
    list1.push(2)
    list1.push(1)

    print("1. Give a Linked List {}, is a palindrome ? : {}".format(
        list1, Solution().isPalindrome(list1.head)
    ))

    # Creating a List
    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(2)
    list1.push(1)

    print("2. Give a Linked List {}, is a palindrome ? : {}".format(
        list1, Solution().isPalindrome(list1.head)
    ))

    # Creating a List
    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    list1.push(3)
    list1.push(2)
    list1.push(1)
    list1.push(1)

    print("3. Give a Linked List {}, is a palindrome ? : {}".format(
        list1, Solution().isPalindrome(list1.head)
    ))
