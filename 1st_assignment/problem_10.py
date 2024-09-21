'''Problem 10: Sum of Even Numbers
Write a Python program that finds and prints the sum of all even numbers between 1 and a number
N (inclusive), where N is provided by the user.'''





N = int(input("Enter a number: "))    # Taking input from the user
e_sum = 0                 # Initialize sum variable

for i in range(2, N + 1, 2):  # Step of 2 ensures only even numbers
    e_sum += i

# Print the result
print(f"The sum of even numbers between 1 and {N} is: {e_sum}")
