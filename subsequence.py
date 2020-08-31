"""
Write an algorithm that prints out all the subsets of three elements of a set of n elements. The elements of this set
are stored in an array S that is the input to the algorithm.
"""

# O(n^k) where n = size of array, and k = subsequence length
# Idea to improve this algorithm: recursion
def print_subsequence_of_three(A):
    saved_indexes = []  # only needed for preprocessing used in 2nd function
    p1 = 0
    while p1 < len(A) - 2:
        p2 = p1 + 1
        while p2 < len(A) - 1:
            p3 = p2 + 1
            while p3 < len(A):
                print(A[p1], A[p2], A[p3])
                saved_indexes.append((p1,p2,p3))
                p3 += 1
            p2 += 1
        p1 += 1
    return saved_indexes

# arr = ['A', 'B', 'C']
# arr = ['A', 'B', 'C', 'D']
arr = ['A', 'B', 'C', 'D', 'E']

index_combos = print_subsequence_of_three(arr)

# With preprocessing, we can print the subsequence in O(n)
def print_subsequence_of_three_2(index_combination_list, A):
    for index_combination in index_combination_list:
        p1 = index_combination[0]
        p2 = index_combination[1]
        p3 = index_combination[2]
        print(A[p1], A[p2], A[p3])

print('\nSubsequence #2')
print_subsequence_of_three_2(index_combos, arr)

