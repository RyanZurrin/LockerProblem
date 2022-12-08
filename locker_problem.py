# 100 lockers numbered 1 to 100 with 100 students lined up in front of those
# 100 lockers. The 1st student opens every locker. The 2nd student closes
# every 2nd locker. The 3rd student changes every 3rd locker; if it’s closed,
# she opens it; if it’s open, she closes it. The 4th student changes every
# fourth locker. The 5th student changes every 5th locker. That same pattern
# continues for all 100 students

# Here’s the question: “Which lockers are left open after all 100 students
# have walked the row of lockers?”

import time

__author__ = "Ryan Zurrin"
__version__ = "0.1.0"


def locker_problem(timing=False, n=1000):
    t0 = time.time()  # start timer

    # get the number of lockers from the user and add 1 to it because we want
    # to start at 1 and not 0
    total_lockers = int(input("Enter the number of lockers and students: ")) + 1
    total_students = total_lockers  # students and lockers are the same value

    # Set all lockers initially to open from 1st student
    lockers_ = [True] * total_lockers

    # Loop through each remaining student starting with the 2nd student
    for student in range(2, total_students + 1):
        # Loop through each locker starting with the first locker each time
        for locker in range(1, total_lockers):
            # If the locker number is a factor of the student number, invert
            # its state
            if locker % student == 0:
                # Change the state of the locker using the not operator
                lockers_[locker] = not lockers_[locker]
        # if timing flag is passed in true then print the time it took to for
        # every n students
        if timing:
            if student % n == 0:
                # print how long it takes to process each 100 students
                print(f"Student {student} took {time.time() - t0} seconds to "
                      f"process")

    # Loop through each locker and print the locker number if it is open
    i = 0  # counter for printing new lines every 25 lockers
    print("\nThe following lockers are open:")
    for locker in range(1, total_lockers):
        # If the locker is open
        if lockers_[locker]:
            # Print the locker number
            if i % 25 == 0:
                print()
            print(locker, end=' ')
            i += 1
    print('\n' * 2)  # print a new line after the last locker number

    if timing:
        print(f"Total time to process {total_students} students is "
              f" {time.time() - t0} seconds")

    return lockers_


def get_factors(lockers_):
    factors_ = {}
    for i in range(1, lockers_ + 1):
        factors_[i] = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors_[i].append(j)
    return factors_


def main():
    """ Main entry point of the app """
    t0 = time.time()
    lockers = locker_problem()
    factors = get_factors(len(lockers))
    print('Open Locker #             Modified by students')
    print('------------------------  ---------------------')
    for i in range(1, len(lockers)):
        if lockers[i]:
            print(f"{i} is open, {' ' * (15 - len(str(i)))} {factors[i]}")

    print()
    t1 = time.time()
    print(f"Time to complete: {t1 - t0}")


if __name__ == "__main__":
    main()
