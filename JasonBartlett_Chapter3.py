# Name: Jason Bartlett
# Assignment: Chapter 3 - Loops and Selection Statements

# The program will ask the user to enter a number from 2 to 100.
# The program will then check if the user's number can be divided evenly by prime numbers starting with 2.
# If the number divides evenly, the program will keep that factor and continue with the smaller number.

number = int(input("Enter a number from 2 to 100: "))
original_number = number
factor = 2

while number > 1:
        if number % factor == 0 :
            if factor == original_number:
                print ("PRIME")
                break
            print(factor)
            number = number // factor
        else:
            factor = factor + 1 
