from collections import deque

dq = deque([1, 2, 3, 4, 5])

# 오른쪽으로 2칸 회전
dq.rotate(2)
print(dq)  # deque([4, 5, 1, 2, 3])

# 왼쪽으로 1칸 회전
dq.rotate(-1)
print(dq)  # deque([5, 1, 2, 3, 4])
