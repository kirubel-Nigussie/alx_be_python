class Calculator:
    def __init__(self):
         pass
    calculation_type = "Arithmetic Operations"

@staticmethod
def add(a, b):
    return a + b

@classmethod
def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
