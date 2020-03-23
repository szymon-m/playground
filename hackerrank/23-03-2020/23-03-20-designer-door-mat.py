# https://www.hackerrank.com/challenges/designer-door-mat/problem

user_input = input()
sizes = user_input.split(" ")
#
n = int(sizes[0])
m = int(sizes[1])
#
# print(n)
# print(m)
#
# n = 9
# m = 27
pattern = ".|."
upper_triangle = list(range((n//2)))  # [0, 1, 2, 3]
lower_triangle = upper_triangle.copy()
lower_triangle.reverse()  # [ 3, 2, 1, 0]

#upper triangle

for i in upper_triangle:
    print(((i*pattern)+pattern+(i*pattern)).center(m,"-"))

#welcome tag

print("WELCOME".center(m,"-"))

#lower triangle

for i in lower_triangle:
    print(((i*pattern)+pattern+(i*pattern)).center(m,"-"))

