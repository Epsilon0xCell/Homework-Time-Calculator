# Homework Time Calculator

import sys


homeworklist = []

# Enter the name of each homework assignment and add it to the list until
# the user types done. The word done is a command, not an assignment, so it
# is not added to the list (previously it was, and the program then asked
# how many minutes "done" would take and counted them in the total).
# End of input (Ctrl-D or a closed pipe) also finishes the list.

print("Enter 'done' when finished.")
print("----------------------------")

while True:
    try:
        homework = input("> ")
    except EOFError:
        break
    if homework.strip() == 'done':
        break
    homeworklist.append(homework)

print("----------------------------")

# Calculate time that it will take for each assignment

# Validate input as a non-negative number of minutes. Decimal values such
# as 1.5 are accepted (previously isnumeric() rejected them and looped
# forever, while isnumeric() also accepts characters such as a superscript
# two that float() then crashed on).

timetaken = 0
print("How many minutes will it take to work on each assignment?")
for item in homeworklist:
    while True:
        try:
            userinput = input(item + ": ")
        except EOFError:
            print("\nInput ended before all times were entered.")
            sys.exit(1)
        try:
            minutes = float(userinput)
        except ValueError:
            print("Please enter a number of minutes, for example 20 or 1.5.")
            continue
        if minutes < 0:
            print("Please enter zero or more minutes.")
            continue
        break
    timetaken = timetaken + minutes

print("----------------------------")

print("It will take you", timetaken, "minutes to complete your homework.")
