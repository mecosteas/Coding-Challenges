# Recursive. Time O(2^n) | Space O(n)
# Notice in the recursive solution that we are returning some sum which is the result
# of another sum made up of additions of 0 or 1. The smaller sums trickle up to the final sum. This is where the
# inefficiency of the recursive solution occurs. Every number, like 10 is the sum of a bunch of ones. It would take 10
# iterations to get to that number and then it occurs again for the f(n - 2) function. So tu add 10 and 9 it would take
# like 19 iterations which each has 2 function calls in it, making it O(2^n)... super inefficient.
def fibonacci(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

# Dynamic. Time O(n) | Space O(1)
def fibonacci_dynamic(n):
# these base cases are just here in case the use inputs 0 or 1. They're not used at all the way it is used
# in the recursive solution
    if n == 0:
        return 0
    if n == 1:
        return 1

# This serves as a type of cache. We only need a variable holding a 0 and another holding a 1 to begin the sequence.
# Each level of the sequence is then cached in these same variables that began as a 0 and 1. This way we avoid having
# to iterate so much like in the recursive solution just to get a 10 from summing a bunch of 1s... it's already cached.
    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return c

print(fibonacci_dynamic(7))