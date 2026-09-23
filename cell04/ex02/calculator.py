#!/usr/bin/env python3

first_number = float(input("Give me the first number: ").strip())
second_number = float(input("Give me the second number: ").strip())

print("Thank you!")
print(f"{first_number:g} + {second_number:g} = {first_number + second_number:g}")
print(f"{first_number:g} - {second_number:g} = {first_number - second_number:g}")
print(f"{first_number:g} / {second_number:g} = {first_number / second_number:g}")
print(f"{first_number:g} * {second_number:g} = {first_number * second_number:g}")