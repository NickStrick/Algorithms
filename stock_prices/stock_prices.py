#!/usr/bin/python

import argparse

# loop through each price
# for each price, find the biggest difference in prices between the prices before the current price in the array
# for each price, loop through all prices before it, find the biggest difference in prices


def find_max_profit(prices):

    max_profit = prices[1] - prices[0]
    for i in range(len(prices)):
        if i == 0:
            continue
        prev_arr = prices[:i]
        max_difference = prices[1] - prices[0]
        for j in range(len(prev_arr)):
            if (prices[i] - prev_arr[j]) > max_difference:
                max_difference = prices[i] - prev_arr[j]
        if max_difference > max_profit:
            max_profit = max_difference

    return max_profit


# print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
