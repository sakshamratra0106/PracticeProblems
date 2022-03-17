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

    def removeElements1(self, val: int) -> Optional[Node]:

        # Remove an element from the LinkedList
        # With time complexity as O(N) and Space Complexity as O(1)

        # Remove first and consequence occurrences of the val
        while self.head and self.head.value == val: self.head = self.head.next

        current = self.head

        while current:
            if current.next and current.next.value == val:
                current.next = current.next.next
            else:
                current = current.next

        return self.head

    def removeElements2(self, val: int) -> Optional[Node]:

        # Remove an element from the LinkedList recursively
        # With time complexity as O(N) and Space Complexity as O(1)

        # TO DO
        # Function Not Working

        # If list is empty
        if not self.head: return None

        # If list is non-empty
        if self.head.value == val:
            self.head = self.removeElements2(self.head.next, val)
        else:
            self.head.next = self.removeElements2(self.head.next, val)
        return self.head


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)

    print("Printing Linked List ll \n {}".format(ll))

    # Remove an element from the linked lists ll and ll1
    ll1 = LinkedList()
    ll1.push(1)
    ll1.push(2)
    ll1.push(6)
    ll1.push(4)
    ll1.push(5)
    ll1.push(6)
    ll1.push(2)

    print("\n#### Going to perform deletion ####")
    removingNumber = 2
    print("\n Given LinkedList is ll \n {}".format(
        ll
    ))
    ll.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll))

    print("\n#### Going to perform deletion ####")
    removingNumber = 4
    print("\n Given LinkedList is ll \n {}".format(
        ll
    ))
    ll.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll))

    print("\n#### Going to perform deletion ####")
    removingNumber = 2
    print("\n Given LinkedList is ll1 \n {}".format(
        ll1
    ))
    ll1.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll1))

    print("\n#### Going to perform deletion ####")
    removingNumber = 6
    print("\n Given LinkedList is ll1 \n {}".format(
        ll1
    ))
    ll1.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll1))

    print("\n#### Going to perform deletion ####")
    removingNumber = 1
    print("\n Given LinkedList is ll1 \n {}".format(
        ll1
    ))
    ll1.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll1))

    print("\n#### Going to perform deletion ####")
    removingNumber = 4
    print("\n Given LinkedList is ll1 \n {}".format(
        ll1
    ))
    ll1.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll1))

    print("\n#### Going to perform deletion ####")
    removingNumber = 5
    print("\n Given LinkedList is ll1 \n {}".format(
        ll1
    ))
    ll1.removeElements1(removingNumber)
    print(" \n Printing Linked List ll1 after removing element {} from linked List \n {}".format(
        removingNumber, ll1))

    # Remove an element from the linked lists ll2
    ll2 = LinkedList()
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)

    print("\n#### Going to perform deletion ####")
    removingNumber = 1
    print("\n Given LinkedList is ll2 \n {}".format(
        ll2
    ))
    ll2.removeElements1(removingNumber)
    print(" \n Printing Linked List ll2 after removing element {} from linked List \n {}".format(
        removingNumber, ll2))

    # Remove an element from the linked lists ll2 using removeElement2()
    ll2 = LinkedList()
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)
    ll2.push(1)

    print("\n#### Going to perform deletion using removeElement2()####")
    removingNumber = 1
    print("\n Given LinkedList is ll2 \n {}".format(
        ll2
    ))
    # ll2.removeElements2(removingNumber)
    print(" \n Printing Linked List ll2 after removing element {} from linked List \n {}".format(
        removingNumber, ll2))