#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they
#will turn 100 years old.
name = input("Enter your name:")
age = int(input("Enter your age:"))
x= 100 - age
year = str((2021-age)+100)
print("Hello " +name + " you shall be turning 100 years after " + str(x) + "years.")
print("Hello " +name + " you shall be turning 100 years in " + year)