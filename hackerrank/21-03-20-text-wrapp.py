# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    print(textwrap.fill(string,max_width))

if __name__ == '__main__':
    user_text_line = input()
    user_wrap_width = int(input())

    wrap(user_text_line,user_wrap_width)