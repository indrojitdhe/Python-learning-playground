""" Author: INDROJIT DHE SHAON
Personal Code: 17
File: check_grade.py """

mark = float(input("Enter your mark: "))

if(mark <= 100 and mark >= 90):
    print("A+")

elif(mark <= 89 and mark >= 80):
    print("A")

elif(mark <= 79 and mark >= 70):
    print("B+")

elif(mark <= 69 and mark >= 60):
    print("B")

elif(mark <= 59 and mark >= 50):
    print("C")

elif(mark <= 49 and mark >= 40):
    print("D")

elif(mark <= 39 and mark >= 33):
    print("Pass")

elif(mark <= 32 and mark >= 0):
    print("F")

elif(mark > 100 and mark < 0):
    print("Enter the correct number")