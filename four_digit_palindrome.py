"""
Let's call an integer a palindrome if it remains the same after reading its digits from right to left. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

Example input #1
1221

Example output #1
YES

Example input #2
1234

Example output #2
NO
"""
def four_digit_panidrome():
    # Read an integer:
    a = int(input())
    n = 0  # length of integer
    i = 0
    # find length of number
    while a // 10 ** i > 0:
        n += 1
        i += 1

    flag = True
    for i in range(1, n):
        # start at last digit and work our way to the first number
        last_num = (a % 10 ** i) // 10 ** (i - 1)
        # start at first number and work our way to the last number
        first_num = (a // 10 ** (n - i)) % 10
        if last_num != first_num:
            flag = False
    if flag:
        print('YES')
    else:
        print('NO')

four_digit_panidrome()