FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
   return (fahrenheit - 32) *FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
   return(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

temp=int(input("Enter the temperature to convert:"))
user_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if user_temp == "C" :
   print(convert_to_fahrenheit(temp))
elif user_temp == "F" :
   print(convert_to_celsius(temp))
else:
   print("Invalid temperature. Please enter a numeric value.")   