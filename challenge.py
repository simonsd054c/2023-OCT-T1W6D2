# Task
# Given an integer, n, perform the following conditional actions:


# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format


# A single line containing a positive integer, n.


# Constraints
# 2 < =n <= 100


# Output Format


# Print Weird if the number is weird. Otherwise, print Not Weird.


# Sample Input 0


# 3
# Sample Output 0


# Weird


n = int(input("Enter a number between 2 and 100: "))

if (n % 2 == 1):
    print("Weird")
else:
    if (n >= 2 and n <= 5):
        print("Not Weird")
    elif (n >= 6 and n <= 20):
        print("Weird")
    else:
        print("Not Weird")