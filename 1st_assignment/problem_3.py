'''Problem 3: Bill Splitter
You and your friends went to a restaurant. The bill is Rs 6570. Write a Python program that asks for
the number of people and splits the bill equally among them. Ensure the output shows how much
each person needs to pay.'''


n=int(input("Eneter the number of friends: ")) # taking input for the number of friends
bill_amount_for_each=6570/n #applying the formula
print("the bill amount for each person is Rs: ",bill_amount_for_each)

