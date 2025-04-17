# add_numbers.py

def get_number(prompt):
     while True:
          try:
               return int(input(prompt))
          except ValueError:
               print("Invalid input! Please enter a valid number.")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

result = num1 + num2
print(f"The sum is: {result}")
