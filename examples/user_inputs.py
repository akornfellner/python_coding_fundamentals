# inputs from user

# input() function
# input() function is used to take input from user
# it takes a string as argument which is printed on screen
# and returns the input as a string

name = input("Enter your name: ")
print("Hello " + name)

x = input("Enter a number: ")
print(2 * x)  # what will this print?

# input() function always returns a string
# if you want to take integer input, you need to convert it

x = int(input("Enter a number: "))
print(2 * x)
