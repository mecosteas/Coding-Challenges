"""
You're given an array of arrays where each subarray holds two integer values and represents an item; the first integer
is the item's value, and the second integer is the item's weight. You're also given an integer representing the maximum
capacity of a knapsack.

Your goal is to fit items in your knapsack without having the sum of their weights exceed the knapsack's capacity, all
the while maximizing their combined value. Note that you only have one of each item.

Write a function that returns the maximized combined value of the items that you should pick as well as an array of the
indices of each item picked.

If there are multiple combination of items that maximize the total value in the knapsack, your function can return
any of them.
"""
def knapsack(items, capacity):
    # items = [[value, weight], [value, weight], ...]
    values = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]  # we added an extra row and column full of 0s
    for i in range(1, len(items) + 1): #
        v = items[i - 1][0]  # items will begin at i - 1 since we are starting i at 1 instead of 0 so we skip row of 0s
        w = items[i - 1][1]
        for c in range(capacity + 1):
            if w > c:
                values[i][c] = values[i - 1][c]
            else:
                values[i][c] = max(values[i - 1][c], values[i - 1][c - w] + v)
    return [values[-1][-1], getKnapsackItems(values, items)]

def getKnapsackItems(values, items):
    sequence = []
    i = len(values) - 1  # the last row
    c = len(values[0]) - 1  # last column
    while i > 0:
        # starting with bottom right value, if it's equal to the value above, this means we pulled the value down,
        # meaning the current item is not actually inthe knapsack, but the previous might be. Thus, update row (i)
        # to be the previous (above) row
        if values[i][c] == values[i - 1][c]:
            i -= 1
        # If we didn't pull down the value from above row, this means the current item is in the knapsack, so add its
        # index, then let's subtract the current item's weight from the current weight so that we can check any other
        # possible item that might still fit in the knapsack
        else:
            sequence.append(i - 1)
            i -= 1
            # ex: we begin at max weight 10, after we save that index, subtract its weight, say 5. 10 - 5 = 5
            # now let's check the above row at capacity 5 and repeat process
            c -= items[i - 1][1]
        # if we're at 0 capacity, stop
        if c == 0:
            break
    return list(reversed(sequence))

items = [[5,3],[10,5],[15,7]]
print(knapsack(items, 10))

"""
You're trying to solve the Knapsack Problem- a common problem in computer science (and in many RPG video games!).

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 

The problem has been solved- but recursively! Now we can't find values for Bags of Holding, which can hold unusually large amounts of weight. Adapt this solution to cache results and solve iteratively.
"""
def knapsack_recursive(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapsack_recursive(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapsack_recursive(W - wt[n - 1], wt, val, n - 1),
                   knapsack_recursive(W, wt, val, n - 1))

wt = [3,5,7]
v = [5,10,15]
n = len(v)
W = 10
print(knapsack_recursive(W, wt, v, n))

def knapsack2(capacity, wt, val, n):
    # items = [[value, weight], [value, weight], ...]
    # make a table w/ items as rows and capacities as columns. Initialize it with 0s. values[row][col] = (item's value)
    # capacities range from 0 to capacity
    values = [[0 for x in range(capacity + 1)] for y in range(n + 1)]  # values is n + 1 by n + 1 square matrix
    for i in range(1, n + 1): #
        v = val[i - 1]  # items will begin at i - 1 since we added an extra row and column of 0s in values[]
        w = wt[i - 1]   # (we are iterating through the range of values[] which is 1 col/row larger than wt/val)
        for c in range(capacity + 1):
            if w > c:
                values[i][c] = values[i - 1][c]
            else:
                values[i][c] = max(values[i - 1][c], values[i - 1][c - w] + v)
    return values[-1][-1]

print(knapsack2(W, wt, v, n))