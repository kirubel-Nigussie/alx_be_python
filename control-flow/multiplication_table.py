# number = int(input("Enter a number to see its multiplication table:"))
number = 5

for num in range(1,11):
    print (f"{number} {"*"} {num} {"="} {number * num}")
