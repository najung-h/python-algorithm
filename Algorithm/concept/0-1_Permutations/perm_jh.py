def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield (arr[i],)
        else:
            for next in permutation(arr[:i] + arr[i+1:], r-1):
                yield (arr[i],) + next


arr = [1,2,3]
print(list(permutation(arr, 2)))

# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]