from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    user_input = input("Enter the number of days to add to the current date:")
    def calculate_future_date(): 
      future_date = current_date + timedelta(user_input) 
      print(future_date.strftime("%Y-%m-%d %H:%M:%S"))
    
    calculate_future_date()

display_current_datetime()