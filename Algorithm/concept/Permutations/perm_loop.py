# {1, 2, 3}의 모든 순열을 구하기 위한 3중 for문

for i in range(1, 4):
    for j in range(1, 4):
        # i와 j가 겹치지 않는 경우에만 다음 단계로
        if i != j:
            for k in range(1, 4):
                # i, j, k가 모두 겹치지 않는 경우 출력
                if i != k and j != k:
                    print(i, j, k)


'''
ouput

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

'''