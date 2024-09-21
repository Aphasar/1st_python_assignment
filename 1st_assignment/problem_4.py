'''Problem 4: Leap Year Checker
Write a program that checks whether a given year is a leap year or not. A year is a leap year if it is:
• Divisible by 4, but not divisible by 100, or
• Divisible by 400.'''


year=int(input("Enter the year: ")) #taking input from the user
if year % 4 == 0 and year % 100 != 0: #using condition to check for leap year
    
    print("Given year is a leap year")
else:                                   
    print("Given year is not a leap year")
