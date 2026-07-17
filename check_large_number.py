""" Author: INDROJIT DHE SHAON
Personal Code: 17
File: check_large_number.py """

number_1 = float(input("Enter the first number: "))      # The first number of the user
number_2 = float(input("Enter the second number: "))     # The second number of the user
number_3 = float(input("Enter the third number: "))     # The third number of the user

if(number_1>number_2 and number_1>number_3):
    print(f"Large number (First number): {number_1}")

elif(number_2>number_1 and number_2>number_3):
    print(f"Large number (Second number): {number_2}")

else:
    print(f"Large number (Third number): {number_3}")