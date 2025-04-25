# This program says hello and asks for my name

print("Hey there")
print("What's your name?") # ask for their name
myName = input()
print("It's good to meet you, " + myName)
print("The length of yor name is:")
print(str(len(myName)) + " characters")
print("What is your age?") # ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year")