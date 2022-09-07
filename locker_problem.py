# 100 lockers numbered 1 to 100 with 100 students lined up in front of those 100 lockers.
# The 1st student opens every locker.
# The 2nd student closes every 2nd locker.
# The 3rd student changes every 3rd locker; if it’s closed, she opens it; if it’s open, she closes it.
# The 4th student changes every fourth locker.
# The 5th student changes every 5th locker.
# That same pattern continues for all 100 students

# Here’s the question: “Which lockers are left open after all 100 students have walked the row of lockers?”


def main():
    # Create a list of 100 lockers with all opened by the first student
    lockers = [True] * 100
    # Loop through each student starting with the second student
    for student in range(2, 101):
        # Loop through each locker starting with the second locker
        for locker in range(1, 100):
            # If the locker number is a multiple of the student number
            if locker % student == 0:
                # Change the state of the locker
                print("student number: ", student, "locker number: ", locker)
                lockers[locker] = not lockers[locker]
    # Loop through each locker
    for locker in range(100):
        # If the locker is open
        if lockers[locker]:
            # Print the locker number
            print(locker + 1, end=' ')
    print()


if __name__ == '__main__':
    main()
