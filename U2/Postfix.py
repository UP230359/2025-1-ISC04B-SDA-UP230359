import math
from stack import Stack
from infix_to_postfix import infix_to_postfix

def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()
    operators = {"+", "-", "*", "/", "^",
                 "log", "sin", "cos", "tan", 
                 "ln", "asin", "acos", "atan", 
                 "alog", "aln"}
    
    for token in tokens:
        if token not in operators:
            try:
                stack.push(float(token))
            except ValueError:
                print(f"Error converting token to number: {token}")
                return None
        else:
            if token in {"+", "-", "*", "/", "^"}:
                b, a = stack.pop(), stack.pop()
                try:
                    result = {
                        "+": a + b,
                        "-": a - b,
                        "*": a * b,
                        "/": a / b,
                        "^": a ** b
                    }[token]
                    stack.push(result)
                except Exception as e:
                    print(f"Error performing operation {token}: {e}")
                    return None
            else:
                x = stack.pop()
                try:
                    result = {
                        "log": math.log10(x),
                        "sin": math.sin(math.radians(x)),
                        "cos": math.cos(math.radians(x)),
                        "tan": math.tan(math.radians(x)),
                        "ln": math.log(x),
                        "asin": math.degrees(math.asin(x)),
                        "acos": math.degrees(math.acos(x)),
                        "atan": math.degrees(math.atan(x)),
                        "alog": 10 ** x,
                        "aln": math.exp(x)
                    }[token]
                    stack.push(result)
                except ValueError as ve:
                    print(f"Math error in {token}({x}): {ve}")
                    return None
                except Exception as e:
                    print(f"Error processing function {token}: {e}")
                    return None
    
    return stack.pop()

# Execution
test_expression = "( 3 + π ) * 2 - ( π / 4 )"
postfix_expr = infix_to_postfix(test_expression)
result = evaluate_postfix(postfix_expr)
print("Expression result:", result)



