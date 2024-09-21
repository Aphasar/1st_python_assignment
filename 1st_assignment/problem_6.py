'''Problem 6: Vowel Counter
Write a Python program that takes a string as input and counts
the number of vowels (a,e,i,o, u) in it. Ignore case sensitivity.'''



user_input = input("Enter a string: ")       # Get input from the user


user_input = user_input.lower()          # Convert to lowercase to ignore case sensitivity

vowel_count = 0      # Initialize a counter for vowels

for char in user_input:        
    if char in 'aeiou':  # Directly checking if the character is a vowel
        vowel_count += 1
print(f"Number of vowels: {vowel_count}")      # Print the total number of vowels
