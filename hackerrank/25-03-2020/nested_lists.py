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


def sorted_by_score_ascending(how_many_scores, name_scores_list):
    db1 = []
    [db1.append([x[0], x[1]]) for x in name_scores_list]
    db1 = sorted(db1, key=lambda x: x[1], reverse=False)
    return db1


def find_second_lowest_ordered_by_name(given_scores_list):
    db1 = []
    db1 = sorted_by_score_ascending(len(given_scores_list), given_scores_list)
    new_db = []
    [new_db.append(item) for item in db1 if item[1] == db1[1][1]]

    new_db = sorted(new_db, key=lambda x: x[0], reverse=False)

    if len(new_db) == 1:
        return new_db[0]
    else:
        return new_db


if __name__ == '__main__':

    db = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        db.append([name, score])

    # print(db)

    ordered_seconds_scores = []
    ordered_seconds_scores = find_second_lowest_ordered_by_name(db)

    for score in ordered_seconds_scores:
        print(score[0])
