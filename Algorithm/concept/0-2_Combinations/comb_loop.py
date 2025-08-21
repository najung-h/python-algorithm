numbers = [1, 2, 3, 4]
n = len(numbers)

# 3개의 원소를 뽑으므로 3중 for문 사용
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            print(numbers[i], numbers[j], numbers[k])


'''
<output>

1 2 3
1 2 4
1 3 4
2 3 4
'''