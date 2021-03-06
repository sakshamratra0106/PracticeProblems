# Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        # Added this flag to reduce detect loop with memory complexity from O(N) to O(1)
        # detectLoop1 has O(N) and detectLoop2 has O(1)
        self.visitedCount = 0


# Linked List Structure
class LinkedList:

    # Function to initialize the linked list
    def __init__(self):
        self.head = None

    # inserting elements to linked list in the beginning
    def push(self, element) -> None:
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    # Alternate to printList Function
    # Also called as Magic function for CLASS's
    # By default called when object of the class is called inside a print(CLASS obj) function

    def __str__(self):

        if not self.detectLoop3():

            # defining a blank res variable
            res = ""

            # initializing ptr to head
            ptr = self.head

            # traversing and adding it to res
            while ptr:
                res += str(ptr.value) + ", "
                ptr = ptr.next

            # removing trailing commas
            res = res.strip(", ")

            # chen checking if
            # anything is present in res or not
            if len(res):
                return "[" + res + "]"
            else:
                return "[]"
        else:
            return "\"Cyclic Linked List has been detected hence not printing." \
                   "Will Enhance the code to print the cyclic Linked Lists in Future.\""

    # Printing the linked list
    def printList(self) -> None:
        temp = self.head
        print("\n HEAD", end="")

        # commenting out since this works only when
        # Linked Lists doesn't have a loop

        # while temp:
        #     print("--", temp.value, end="")
        #     temp = temp.next

        # To Do #
        # Implement changes to accommodate
        # if linkedList is looped or is looped or is cycled
        # at that time also it should work

        if self.detectLoop3():
            return None
        else:
            while temp:
                print("--", temp.value, end="")
                temp = temp.next

    # Detect Loop in LinkedList with O(N)
    def detectLoop1(self) -> None:

        # Checks each element if it exists in Set s
        # Time Complexity O(N) and Memory O(N)

        s = set()
        temp = self.head

        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)

            temp = temp.next

        return False

    # Detect Loop in LinkedList with O(N)
    def detectLoop2(self) -> None:

        # Checks each element if it exists in Set s
        # Time Complexity O(N) and Memory O(1)

        # This required a fundamental change in NODE class structure
        # to have one more attribute to contain visitedCount

        temp = self.head

        while temp:
            if temp.visitedCount > 0:
                return True
            else:
                temp.visitedCount += 1

            temp = temp.next

        return False

        # Detect Loop in LinkedList with O(N)

    def detectLoop3(self) -> None:

        # Implementation of Floyd???s Cycle-Finding Algorithm:
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


if __name__ == "__main__":
    # Creating the Linked List and Inserting elements Method One
    Llist = LinkedList()
    Llist.head = Node(1)
    Llist.head.next = Node(2)
    Llist.head.next.next = Node(3)

    print("Printing First Linked List ", Llist)


    # Creating the Linked List and Inserting elements Method Two

    Llist1 = LinkedList()
    Llist1.head = Node(5)
    first = Node(6)
    second = Node(7)
    third = Node(8)

    Llist1.head.next = first
    first.next = second
    second.next = third
    third.next = first

    print("\n Printing Second Linked List ",Llist1)
    # Since to detect loop in a Linked List
    # had to create a list with a loop and after creating a loop and printing
    # it will go in an infinite loop hence commenting this out
    # Incase want to use print condition again remove or comment line number 70
    # i.e line 70. third.next = first

    # print("commented out this part because of infinite loop")

    # Corrected the code if conditions to return exceptions to cyclic LinkedList
    # Llist1.printList()

    # Creating the Linked List and Inserting elements Method Three
    Llist = LinkedList()
    Llist.push(1)
    Llist.push(2)
    Llist.push(3)
    Llist.push(4)
    Llist.push(5)
    print("\nPrinting Third Linked List ",Llist)

    # Checking loop with variable Llist1
    if Llist1.detectLoop1():
        print("\n Linked List {} has loop in it (using detectLoop1)? {}".format(
            Llist1, True
        ))
    else:
        print("\nLinked List {} has loop in it  (using detectLoop1)? {}".format(
            Llist1, False
        ))

    # Checking loop with variable Llist
    if Llist.detectLoop1():
        print("\nLinked List {} has loop in it  (using detectLoop1)? {}".format(
            Llist, True
        ))
    else:
        print("\nLinked List {} has loop in it  (using detectLoop1)? {}".format(
            Llist, False
        ))

    # Checking loop with variable Llist1
    if Llist1.detectLoop2():
        print("\nLinked List {} has loop in it  (using detectLoop2)? {}".format(
            Llist1, True
        ))
    else:
        print("\nLinked List {} has loop in it   (using detectLoop2)? {}".format(
            Llist1, False
        ))

    # Checking loop with variable Llist
    if Llist.detectLoop2():
        print("\nLinked List {} has loop in it   (using detectLoop2)? {}".format(
            Llist, True
        ))
    else:
        print("\nLinked List {} has loop in it   (using detectLoop2)? {}".format(
            Llist, False
        ))

    # Checking loop with variable Llist1
    if Llist1.detectLoop3():
        print("\nLinked List {} has loop in it (using detectLoop3)? {}".format(
            Llist1, True
        ))
    else:
        print("\nLinked List {} has loop in it  (using detectLoop3)? {}".format(
            Llist1, False
        ))

    # Checking loop with variable Llist
    if Llist.detectLoop3():
        print("\nLinked List {} has loop in it  (using detectLoop3)? {}".format(
            Llist, True
        ))
    else:
        print("\nLinked List {} has loop in it  (using detectLoop3)? {}".format(
            Llist, False
        ))


    # Pretty print with magic function __str__
    # when List doesn't have cycle in it
    print("Pretty print with magic function __str__ = ", Llist)

    # when List does have cycle in it
    # Falls into infinite loop
    print("Pretty print with magic function __str__ when List does have cycle in it = ", Llist1)
