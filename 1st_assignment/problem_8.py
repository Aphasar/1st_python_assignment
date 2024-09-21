'''Movie Ticket Price Calculator
Write a program that calculates the price of a movie ticket based on the user's age. Ticket prices are
as follows:
• Age under 18: Rs 108
• Age 18-60: Rs 450
• Age above 60: Rs 150'''




age=int(input("Enter your age: ")) #taking input as age from user
if age<18:   #first condition
    print("the price of the ticket is Rs 108")
elif age>=18 and age<60: #second condition 
    print("the price of the ticket is Rs 450")
else:
    print("the price of the ticket is Rs 150")
 
