def perform_operation(num1: float, num2: float, operation):
    if (operation == "add"):
        return num1 + num2
    elif (operation == "subtract"):
        return num1 - num2
    elif (operation == "divide"):
        if (num2 == 0):
            print("give me a non zero number")
        else:
            return num1 / num2
    elif (operation == "multiply"):
        return num1 * num2

 