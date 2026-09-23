#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n").strip())
second_number = int(input("Enter the second number:\n").strip())

result = first_number * second_number

print(f"{first_number} x {second_number} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")