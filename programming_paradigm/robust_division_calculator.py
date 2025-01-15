def safe_divide(numerator, denominator):
    try:
       result = numerator/denominator 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        return f"The result of the division is {result}"

