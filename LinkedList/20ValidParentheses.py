from LinkedList import *


def isValidParentheses(s: str) -> bool:
    # Constraints and knowledge Base
    parenthesesMapping = {")": "(", "]": "[", "}": "{"}
    openingBrackets = ["(", "[", "{"]
    closingBrackets = [")", "]", "}"]

    # Checking if valid parenthessis only if it is not none
    if s:
        # First char should be opening bracket else False
        if s[0] in openingBrackets:
            paranthesesStack = LinkedList()

            # Start Processing one by one
            for char in s:

                # If opening bracket push into stack
                if char in openingBrackets:
                    paranthesesStack.push(char)

                # If closing bracket and stack is not none else False
                # Find if its opening bracket is in top of stack else False
                elif char in closingBrackets and paranthesesStack.head:
                    if parenthesesMapping[char] == paranthesesStack.head.value:
                        paranthesesStack.pop()
                    else:
                        return False
                else:
                    return False

            # if stack is not empty yet return false
            if paranthesesStack.head:
                return False

        # Starting bracket is not in ["(","[","{"]
        else:
            return False

        # All checks have passed so return True

    return True


class Solution:
    pass


if __name__ == "__main__":

    expression = "()[]{}"

    print("1. Expression {} is a valid expression ? : {}".format(
        expression, isValidParentheses(expression)
    ))

    expression = "(]"

    print("2. Expression {} is a valid expression ? : {}".format(
        expression, isValidParentheses(expression)
    ))

    expression = "(([]))"

    print("3. Expression {} is a valid expression ? : {}".format(
        expression, isValidParentheses(expression)
    ))

    expression = "(){}}{"

    print("4. Expression {} is a valid expression ? : {}".format(
        expression, isValidParentheses(expression)
    ))