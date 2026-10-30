# Homework Time Calculator
#
# I wrote this as one flat script on purpose. It runs top to bottom in
# the order a person uses it: list first, times second, total last.
# There is no main guard, so importing this file would also start asking
# questions. I only ever run it directly, so I left it that way.

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
        # I let EOF end the name list quietly, because a short list is
        # still a valid answer here. The time loop below treats EOF
        # differently on purpose: a missing time is not a zero.
        break
    # I compare after strip(), so " done " still ends the list, but I do
    # not fold case. "Done" counts as an assignment name. I measured
    # that with scripted input: it gets asked for minutes like any
    # other entry.
    if homework.strip() == 'done':
        break
    # I do not reject empty names either. A blank line becomes an
    # assignment with an empty name and gets a bare ": " prompt in the
    # next loop. It looks odd in the output and the total stays right.
    homeworklist.append(homework)

print("----------------------------")

# Calculate time that it will take for each assignment

# Validate input as a non-negative number of minutes. Decimal values such
# as 1.5 are accepted (previously isnumeric() rejected them and looped
# forever, while isnumeric() also accepts characters such as a superscript
# two that float() then crashed on).

# I start the total as the int 0, so an empty list prints "0 minutes"
# while any real entry turns it into a float and the total prints like
# 30.0. That mismatch is in the output today, and the README example
# shows the float form.

timetaken = 0
print("How many minutes will it take to work on each assignment?")
for item in homeworklist:
    while True:
        try:
            userinput = input(item + ": ")
        except EOFError:
            # I exit 1 here instead of printing a partial total. A total
            # built from half the times would look real and be wrong.
            print("\nInput ended before all times were entered.")
            sys.exit(1)
        try:
            minutes = float(userinput)
        except ValueError:
            print("Please enter a number of minutes, for example 20 or 1.5.")
            continue
        # float() also accepts "nan" and "inf", and neither is caught
        # here: nan < 0 is False, so both pass the check below and the
        # total prints as nan or inf. I measured both with scripted
        # input. The check below only guards real negative numbers.
        if minutes < 0:
            print("Please enter zero or more minutes.")
            continue
        break
    timetaken = timetaken + minutes

print("----------------------------")

print("It will take you", timetaken, "minutes to complete your homework.")
