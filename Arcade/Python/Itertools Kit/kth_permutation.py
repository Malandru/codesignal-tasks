from itertools import permutations

def kthPermutation(numbers, k):
    return list(permutations(numbers))[k - 1]

numbers = [1, 2, 3, 4, 5]
k = 4
print(kthPermutation(numbers, k))