# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
def first_non_consecutive(arr):
    if len(arr) > 1:
        step = arr[1] - arr[0]

    for i in range(len(arr)):

        print(arr[i] - arr[i - 1])
        print(step)

        if (arr[i] - arr[i - 1]) > 1:
            return arr[i]