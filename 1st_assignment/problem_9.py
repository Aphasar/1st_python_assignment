'''Problem 9: Multiplication Table Generator
Write a program that takes an integer input from the user and prints the multiplication table for that
number up to 10'''



n=int(input("Enter an integer"))   #taking input from user
for i in range(1,11):     # ensuring only number from 1 to 10
    print(n*i)
