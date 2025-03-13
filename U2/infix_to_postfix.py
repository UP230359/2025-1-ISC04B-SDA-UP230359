from stack import Stack
from queue import Queue
import math
import re

def add_spaces(expression):
    return " ".join(re.findall(r'\d+\.\d+|\d+|[+\-*/^()]|\w+', expression))

def infix_to_postfix(expression):
    expression = add_spaces(expression)
    precedence = { 
        "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 0,
        "log": 4, "ln": 4, "sin": 4, "cos": 4, "tan": 4,
        "alog": 4, "aln": 4, "asin": 4, "acos": 4, "atan": 4
    }
    
    stack = Stack()
    queue = Queue()
    tokens = ["("] + expression.split() + [")"]
    
    for token in tokens:
        if token == "(":
            stack.push(token)
        elif token == ")":
            while stack.peek() != "(":
                queue.enqueue(stack.pop())
            stack.pop()
        elif token in precedence:
            while (not stack.is_empty() and stack.peek() != "(" and precedence[token] <= precedence[stack.peek()]):
                queue.enqueue(stack.pop())
            stack.push(token)
        elif token.lower() == "π" or token.lower() == "pi":
            queue.enqueue(math.pi)
        else:
            try:
                queue.enqueue(float(token))
            except ValueError:
                print(f"Error: {token} is not valid.")
    
    return " ".join(str(queue.dequeue()) for _ in range(queue.size))