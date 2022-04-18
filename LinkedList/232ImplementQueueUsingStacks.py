class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:

    # Rear(push happens) is used for insert/push works in the head of the Singly Linked List
    # front(pop happens) is used for deletion/removing works on the end of the Singly Linked List

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    # Is the Queue empty
    # def isEmpty(self):
    #     return self.front is None

    def __str__(self) -> str:
        # Magic function to print the Queue
        # OR in general used to return a String when called in a print() function
        printLinkedList = "FRONT(POPS)<--"
        temp = self.front
        while temp:
            printLinkedList += str(temp.value) + "<--"
            temp = temp.next

        printLinkedList += "REAR(PUSH)"

        return printLinkedList

    # Push an element in its rear
    def push(self, x: int) -> None:
        # Create a new node
        new_node = Node(x)

        # check if the queue is empty
        # if yes change both the pointer to new node
        if self.rear is None:
            self.rear = self.front = new_node
            return

        # if queue already has data
        # point end node to new node and rear pointer to new node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Remove element from front
    def pop(self) -> int:

        # If queue is empty return none
        if self.empty():
            return

        # If queue is has data
        # move its fronts' pointer to next pointer and
        # save the top Node in temp variable
        # so that we can return its value as popped in the end
        temp = self.front
        self.front = self.front.next

        # if after pop, queue is empty i.e. front is none
        # make rear none as well
        if self.front is None:
            self.rear = None

        # return popped value
        return temp.value

    # to check first element on the front to be popped
    def peek(self) -> int:
        return self.front.value

    # is queue empty ?
    def empty(self) -> bool:
        return self.front is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)

    print(obj)
    print(obj.pop())
    print(obj)
    # print(obj.isEmpty())
    print(obj.peek())
    print(obj.empty())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())