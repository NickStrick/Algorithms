#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# Spec
#   for each cookie, loop through the

# yummy_count = 0


# def eating_cookies(n, cache=None):
#     global yummy_count
#     if n > 0:
#         if n == 1:
#             return 1
#         else:
#             for i in range(n):
#                 curr = i + eating_cookies(n-1)
#                 if curr == n:
#                     print('combo')
#                     yummy_count += 1
#     return yummy_count
def eating_cookies(n,  rest=[], cache=None):
    # loop through all posiblities
    # if  possiblity can
    numbers = []
    for i in range(n):
        numbers.append(i+1)

    def sum_cookies(numbers, target, rest=[]):
        if rest:
            s = sum(rest)
        else:
            s = 0

    # check if the s is qual to n
        if s == target:
            print(1)
        if s >= target:
            return  # if above number, dont continue

        for i in range(len(numbers)):
            remaining = numbers[i+1]
            sum_cookies(remaining, target, rest.append(numbers[i]))
    sum_cookies(numbers, n)


# print(eating_cookies(4))
# print(eating_cookies(1), 1)
# print(eating_cookies(2), 2)
print(eating_cookies(5), 13)
# print(eating_cookies(10), 274)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
