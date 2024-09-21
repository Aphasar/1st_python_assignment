'''Write a Python program that takes input for principal (P), rate of interest (R), and time (T) in years,
and calculates the simple interest using the formula:
Simple Interest=P×R×T/ 100'''

p=float(input("Enter the principle: "))#taking input from user
r=float(input("Enter the interest rate: "))#taking input from user
t=float(input("enter the time: "))#taking input from user
simple_interest=(p*t*r)/100    #initializing formula of simple interest
print("the interest is: ",simple_interest)
