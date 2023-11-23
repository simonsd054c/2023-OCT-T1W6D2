# 2 states - State1 and State2 - take input from the user
state = input("Enter your state: ")

# take age from the user
age = int(input("Enter your age: "))

# In state1
# age >=18 can vote
# age < 18 can't vote

# In state2
# age >=21 can vote
# age < 21 can't vote

if(state.lower() == "state1"):
    if(age >= 18):
        print("Can vote in state 1")
    else:
        print("Can't vote in state 1")
else:
    if(age >= 21):
        print("Can vote in state 2")
    else:
        print("Can't vote in state 2")
