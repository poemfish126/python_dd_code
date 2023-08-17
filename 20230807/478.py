class Calculator:

    def calculate(self, a: int, op: str, b: int) -> int:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return int(a / b)
        else:
            return 0

c = Calculator()
print(c.calculate(3, '+', 2))


