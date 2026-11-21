class Stack:
    def init(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if len(self._items) == 0:
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if len(self._items) == 0:
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def len(self):
        return len(self._items)


def is_balanced(text):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if len(stack) == 0:
                return False
            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def evaluate_postfix(tokens):
    stack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**', '^']

    for token in tokens:
        if token not in operators:
            try:
                stack.push(float(token))
            except (ValueError, TypeError):
                raise ValueError("Malformed postfix expression")
        else:
            if len(stack) < 2:
                raise ValueError("Malformed postfix expression")

            right = stack.pop()
            left = stack.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                if right == 0:
                    raise ValueError("Division by zero")
                result = left / right
            elif token == '//':
                if right == 0:
                    raise ValueError("Division by zero")
                result = left // right
            elif token == '%':
                result = left % right
            else:
                result = left ** right

            stack.push(result)

    if len(stack) != 1:
        raise ValueError("Malformed postfix expression")

    return stack.pop()


def infix_to_postfix(tokens):
    stack = Stack()
    output = []

    precedence = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '//': 2, '%': 2,
        '^': 3, '**': 3
    }

    right_associative = ['^', '**']

    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            while len(stack) > 0 and stack.peek() != '(':
                output.append(stack.pop())

            if len(stack) == 0:
                raise ValueError("Mismatched parentheses")

            stack.pop()
        elif token in precedence:
            while len(stack) > 0 and stack.peek() in precedence:
                top = stack.peek()

                if (precedence[top] > precedence[token] or
                    (precedence[top] == precedence[token]
                     and token not in right_associative)):
                    output.append(stack.pop())
                else:
                    break

            stack.push(token)
        else:
            output.append(token)

    while len(stack) > 0:
        if stack.peek() == '(':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())

    return output


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack:", s._items)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Stack after pop:", s._items)
print("Length:", len(s))

print("Balanced:", is_balanced("(a+b)"))
print("Balanced:", is_balanced("((a+b)"))
print("Balanced:", is_balanced("{[()]}"))
print("Balanced:", is_balanced("([)]"))

postfix = ["2", "3", "+", "4", "*"]
print("Postfix:", postfix)
print("Result:", evaluate_postfix(postfix))

infix = ["2", "+", "3", "*", "4"]
result = infix_to_postfix(infix)
print("Infix:", infix)
print("Postfix:", result)
print("Evaluation:", evaluate_postfix(result))
