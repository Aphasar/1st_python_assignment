'''Problem 2: Temperature Conversion
Write a program that converts a temperature from Celsius to Fahrenheit. The formula for conversion
is:
Where C is the temperature in Celsius and F is the temperature in Fahrenheit'''


c=float(input("Enter temp in celcius: ")) #taking input as temprature from user
Fahrenheit=(c*9/5)+32  # initializing the formula to convert from C to F
print("temp in Fahrenheit is: ",Fahrenheit)
