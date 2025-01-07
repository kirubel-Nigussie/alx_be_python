def perform_operation(num1, num2, operation):
    if (operation == "add"):
        return num1 + num2
    elif (operation == "subtract"):
        return num1 - num2
    elif (operation == "multiply"):
        return num1 * num2
    elif num2 == 0:
        return "give me a non zero number"

    elif (operation == "divide"):
        return num1 / num2
    

 