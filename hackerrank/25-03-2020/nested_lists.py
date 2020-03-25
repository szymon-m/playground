# https://www.hackerrank.com/challenges/nested-list/problem
#
# lists problem and dictionary version Given the names and grades for each student in a Physics class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a
# new line.
#
# Input Format
#
# The first line contains an integer, , the number of students. The  subsequent lines describe each student over
# lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students,
# order their names alphabetically and print each one on a new line.
import operator

if __name__ == '__main__':

    db = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        db.append([name, score])

    #   1. playing with sorted
    #
    #   sorted(iterable, *, key=None, reverse=False)
    #
    #   Return a new sorted list from the items in iterable. Has two optional
    #   arguments which must be specified as keyword arguments.
    #
    #   key specifies a function of one argument that is used
    #   to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is
    #   None (compare the elements directly).
    #
    #   reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

    # db = sorted(db, key=operator.itemgetter(1), reverse=True)

    second_element = lambda element: element[1]

    db = sorted(db, key=second_element, reverse=True)

    print(db)
