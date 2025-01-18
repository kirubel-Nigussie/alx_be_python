def safe_divide(numerator, denominator):
    try:
       num = float(numerator)
       denom = float(denominator)
       result = num / denom
       return f"The result of the division is {result:.2f}"
       
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    

