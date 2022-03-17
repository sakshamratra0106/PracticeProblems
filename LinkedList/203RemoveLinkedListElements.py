from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Inserting new node in Linked List in the top
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Printing the Linked List
    # Given it is not cyclic linked List
    # Else it will fall into a loop
    def __str__(self):
        linkedlist = "HEAD--> "
        temp = self.head
        while temp:
            linkedlist += str(temp.value) + "--> "
            temp = temp.next

        linkedlist += "None"

        return linkedlist

    def removeElements(self, val: int) -> Optional[Node]:
        pass


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)

    print(ll)
