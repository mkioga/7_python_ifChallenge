
# ======================
# 7_ifChallenge.py:
# ======================


# write a small program to ask for a name and age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a polite message refusing them entry


name = input("What is your name: ")
age = int(input("What is your age: "))

if 18 < age < 31:
    print("Hi {0}, Welcome to our 18-30 holiday".format(name))
else:
    print("Sorry {0}, You are not eligible for our 18-30 holiday".format(name))
