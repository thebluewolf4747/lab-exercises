""" CALCULATOR """
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calc = Calculator()

print(calc.add(1, 2))
print(calc.subtract(1, 2))
print(calc.multiply(1, 2))
print(calc.divide(1, 2))