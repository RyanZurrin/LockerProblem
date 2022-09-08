# 100 lockers numbered 1 to 100 with 100 students lined up in front of those 100 lockers.
# The 1st student opens every locker.
# The 2nd student closes every 2nd locker.
# The 3rd student changes every 3rd locker; if it’s closed, she opens it; if it’s open, she closes it.
# The 4th student changes every fourth locker.
# The 5th student changes every 5th locker.
# That same pattern continues for all 100 students

# Here’s the question: “Which lockers are left open after all 100 students have walked the row of lockers?”


def locker_problem():
    # get as input from user the number of lockers and students
    # create a list of lockers with the number of lockers
    # create a list of students with the number of students

    total_lockers = int(input("Enter the number of lockers: "))
    total_students = int(input("Enter the number of students: "))

    # Create a list of 100 lockers with all opened by the first student
    lockers = [True] * total_lockers
    # Loop through each student starting with the second student
    for student in range(2, total_students + 1):
        # Loop through each locker starting with the second locker
        for locker in range(1, total_lockers):
            # If the locker number is a multiple of the student number
            if locker % student == 0:
                # Change the state of the locker
                lockers[locker] = not lockers[locker]
    # Loop through each locker
    for locker in range(1, total_lockers):
        # If the locker is open
        if lockers[locker]:
            # Print the locker number
            print(locker, end=' ')
    print()
    return lockers


def get_factors(lockers):
    factors = {}
    for i in range(1, lockers + 1):
        factors[i] = []
        for j in range(1, i + 1):
            if i % j == 0:
                factors[i].append(j)
    return factors

lockers = locker_problem()
factors = get_factors(len(lockers))
for i in range(1, len(lockers)):
    if lockers[i]:
        print(f"Locker {i} is open. Factors: {factors[i]}")
