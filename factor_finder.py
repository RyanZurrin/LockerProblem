# class to find and track factors between two numbers (start, end),
# Supports methods that allow a user to easily find what numbers have a given
# number of factors including what those factors are, as well as provides
# easy methods to find the numbers that contain the most as well as the least
# number of factors.

# set the author and version
__author__ = "Ryan Zurrin"
__version__ = "0.1.0"


class FactorFinder:
    def __init__(self, start_number=1, end_number=100):
        self.start_number = start_number
        self.end_number = end_number
        self.factors = {}
        self.find_factors()

    def find_factors(self):
        for i in range(self.start_number, self.end_number + 1):
            self.factors[i] = []
            for j in range(1, i + 1):
                if i % j == 0:
                    self.factors[i].append(j)

    def get_factors(self, number):
        return self.factors[number]

    def get_numbers_with_factors(self, number_of_factors):
        numbers = []
        for i in range(self.start_number, self.end_number + 1):
            if len(self.factors[i]) == number_of_factors:
                numbers.append(i)
        return numbers

    def get_numbers_with_max_factors(self):
        """ find what numbers contain the most factors and return that number
        along with its factors """
        max_factors = 0
        max_factors_number = -1
        results = {}
        for i in range(self.start_number, self.end_number + 1):
            if len(self.factors[i]) > max_factors:
                max_factors = len(self.factors[i])
                max_factors_number = i
        results[max_factors_number] = self.factors[max_factors_number]
        for i in range(self.start_number, self.end_number + 1):
            if len(self.factors[i]) == max_factors and i != max_factors_number:
                results[i] = self.factors[i]
        return results

    def get_numbers_with_min_factors(self):
        """ find what numbers contain the least factors and return that number
        along with its factors """
        min_factors = self.end_number
        min_factors_number = -1
        results = {}
        for i in range(self.start_number, self.end_number + 1):
            if len(self.factors[i]) < min_factors:
                min_factors = len(self.factors[i])
                min_factors_number = i
        results[min_factors_number] = self.factors[min_factors_number]
        for i in range(self.start_number, self.end_number + 1):
            if len(self.factors[i]) == min_factors and i != min_factors_number:
                results[i] = self.factors[i]
        return results


# test the class with numbers between 5 and 200
ff = FactorFinder(5, 200)
print(ff.get_factors(100))
print(ff.get_numbers_with_factors(12))
print(ff.get_numbers_with_factors(3))
print(ff.get_numbers_with_max_factors())
print(ff.get_numbers_with_min_factors())
