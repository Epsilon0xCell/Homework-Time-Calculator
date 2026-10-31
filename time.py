# Homework Time Calculator
#
# I wrote this as one flat script on purpose. It runs top to bottom in
# the order a person uses it: list first, times second, total last.
# It now sits inside main() so importing the file for tests does not
# start asking questions; running it directly behaves as before.

import math
import sys


def read_minutes(item):
    """Ask until I get a usable minute count for one assignment.

    Returns None when the input ends early. A total built from half
    the times would look real and be wrong, so the caller treats a
    missing time as a failed run instead of as zero.
    """
    while True:
        try:
            userinput = input(item + ": ")
        except EOFError:
            return None
        try:
            minutes = float(userinput)
        except ValueError:
            print("Please enter a number of minutes, for example 20 or 1.5.")
            continue
        # float() also accepts "nan" and "inf". Neither is a duration,
        # and nan used to slip past the negative check because
        # nan < 0 is False, so the total printed as nan. isfinite
        # closes both in one test.
        if not math.isfinite(minutes):
            print("Please enter a finite number of minutes.")
            continue
        if minutes < 0:
            print("Please enter zero or more minutes.")
            continue
        return minutes


def main():
    homeworklist = []

    print("Enter 'done' when finished.")
    print("----------------------------")

    while True:
        try:
            homework = input("> ")
        except EOFError:
            # I let EOF end the name list quietly, because a short
            # list is still a valid answer here.
            break
        # I compare after strip() and folding case, so "Done" and
        # " done " end the list too. The first version folded nothing,
        # so a capital Done became an assignment I then had to time.
        if homework.strip().lower() == "done":
            break
        # Blank lines are skipped instead of becoming assignments
        # with an empty name and a bare ": " prompt in the next loop.
        if not homework.strip():
            continue
        homeworklist.append(homework)

    print("----------------------------")

    timetaken = 0
    print("How many minutes will it take to work on each assignment?")
    for item in homeworklist:
        minutes = read_minutes(item)
        if minutes is None:
            print("\nInput ended before all times were entered.")
            return 1
        timetaken = timetaken + minutes

    print("----------------------------")
    # Whole totals print without the .0 the float sum used to add,
    # so 30 minutes reads as 30, not 30.0. Fractional totals keep
    # their digits.
    total_text = str(int(timetaken)) if float(timetaken).is_integer() else str(timetaken)
    print("It will take you", total_text, "minutes to complete your homework.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
