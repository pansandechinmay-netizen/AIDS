
# Stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push element
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop element
    def pop(self):
        if self.top is None:
            raise ValueError("Stack Underflow")

        data = self.top.data
        self.top = self.top.next
        return data

    # Check empty
    def is_empty(self):
        return self.top is None


# Evaluate postfix expression
def evaluate_postfix(expression):
    stack = Stack()

    for token in expression.split():
        if token.lstrip("-").isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                stack.push(a / b)
            elif token == '^':
                stack.push(a ** b)
            else:
                raise ValueError("Invalid operator: " + token)

    if stack.is_empty():
        raise ValueError("Invalid postfix expression")

    result = stack.pop()

    if not stack.is_empty():
        raise ValueError("Invalid postfix expression")

    return result


# Main program
expression = input(
    "Enter postfix expression (space-separated): "
)

try:
    result = evaluate_postfix(expression)
    print("Result =", result)
except (ValueError, OverflowError) as error:
    print("Error:", error)
