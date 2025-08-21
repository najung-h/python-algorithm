import itertools

arr = [1, 2, 3, 4]

permutations = list(itertools.permutations(arr, 2))

print(permutations)
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), 
#        (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]



from itertools import permutations
arr = [1, 2, 3, 4]
perm = list(permutations(arr, 2))
print(perm)
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), 
#       (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
