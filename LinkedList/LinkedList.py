from typing import Optional


class Node:

    # Node of the Linked List
    # Has two elements in every node
    # 1. Value
    # 2. next = Pointer to the next node

    # TODO
    ## Make Node available for any kind of Data Type

    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:

    # Linked List Implementation
    # Had a Head which has the first elements'
    # location initialized as None when created

    def __init__(self, head=None):
        # Initializing the Head as None when declared
        self.head = head

    def __str__(self) -> str:
        # Magic function to print the Linked List
        # OR in general used to return a String when called in a print() function

        if self.detectLoop():
            return "\"A Cyclic Linked List has been detected. Hence can not print.\""
        else:
            printLinkedList = "Head-->"
            temp = self.head
            while temp:
                printLinkedList += str(temp.value) + "-->"
                temp = temp.next

            printLinkedList += str(temp)

            return printLinkedList

    def push(self, value: int) -> None:

        # Inserting the values/Nodes in the beginning
        # everytime called with a Value

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:

        # removing the top value
        # as in stack data structure

        # Pop only if the Linked List is non-empty
        if self.head:

            # poped Value
            poped_value = self.head.value
            self.head = self.head.next

        # If the listed list/Stack is empty
        # return none
        else:
            return None

        return poped_value

    def detectLoop(self) -> None:

        # Implementation of Floyd’s Cycle-Finding Algorithm:
        # https://www.youtube.com/watch?v=Aup0kOWoMVg

        # Checks each element if it exists in Set s
        # Time Complexity O(N) and Memory O(1)

        # This required a single extra element to store
        # an old node to match with the next node

        fast, slow = self.head, self.head
        while fast and slow:
            slow = slow.next
            fast = fast.next

            # Uncomment to debug the code
            # print("1. ", slow.value, "--", fast.value)

            if fast:
                fast = fast.next
            else:
                return False

            # Uncomment to debug the code
            # print("2. ",slow.value,"--",fast.value)

            if fast == slow:
                return True
        return False

    def removeElements(self, val: int) -> Optional[Node]:

        # Remove an element from the LinkedList
        # With time complexity as O(N) and Space Complexity as O(1)

        # Remove first and consecutive occurrences of the val
        while self.head and self.head.value == val:
            self.head = self.head.next

        current = self.head

        while current:
            if current.next and current.next.value == val:
                current.next = current.next.next
            else:
                current = current.next

        return self.head


def reverseList(head: Optional[Node]) -> Optional[Node]:
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

        # For Debugging
        # print(reversesList)
        # print(temp.value)

    return reversedList


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
