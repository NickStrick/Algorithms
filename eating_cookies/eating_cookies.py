#!/usr/bin/python
'''
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
'''

# lecture -----------------------------------------------------------------------------------
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
'''
0
--------------
1

1
--------------
1
2 
--------------
1,1 
2

3
--------------
1,1,1 
1,2 
2,1 
3

4
--------------
1,1,1,1 
1,1,2 
1,2,1 
2,1,1 
2,2 
1,3 
3,1

5
--------------
1,1,1,1,1
1,1,1,2 
1,1,2,1 
1,2,1,1 
2,1,1,1 
1,1,3 
1,3,1 
3,1,1 
1,2,2 
2,1,2 
2,2,1 
2,3 
3,2

1,1,1,1,1
  1,1,1,2
    1,2,2
    1,1,3
      2,3

Find all combinations of 1,2,3 that add up to n
Find all possible orderings of those combinations

look at the ways to eat (n-1) cookies, then eat one more
now look at the ways to eat (n-2) cookies, then eat 2 at once
now look at the ways to eat (n-3) cookies, then eat 3 at once
'''

# Spec
#   for each cookie, loop through the


def eating_cookies(n, cache=None):

    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:

        one = eating_cookies(n-1)
        two = eating_cookies(n-2)
        three = eating_cookies(n-3)
        return one+two+three

    # result.append(one)
    # result.append(two)
    # result.append(three)
print(eating_cookies(0), 1)
print(eating_cookies(5), 13)
print(eating_cookies(4), 7)
print(eating_cookies(1), 1)
print(eating_cookies(2), 2)
print(eating_cookies(10), 274)
# print(eating_cookies(50, [0 for i in range(51)]), 10562230626642)
# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
