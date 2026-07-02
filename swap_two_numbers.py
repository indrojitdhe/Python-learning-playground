""" Author: INDROJIT DHE SHAON
Personal Code: 17
File: swap_two_numbers.py """

num_1 = float(input("Enter the first number: "))            # The first number of the user
num_2 = float(input("Enter the second number: "))            # The second number of the user

print(f"Before swapping, Number 1 = {num_1} & Number 2 = {num_2}")

num_1,num_2 = num_2,num_1

print(f"After swapping, Number 1 = {num_1} & Number 2 = {num_2}")