from collections import deque

# 초기 deque 생성
dq = deque([10, 20, 30])
print(f"초기 상태: {dq}")
# 초기 상태: deque([10, 20, 30])

# 1. append(): 오른쪽 끝에 40 추가
dq.append(40)
print(f"append(40) 후: {dq}")
# append(40) 후: deque([10, 20, 30, 40])

# 2. appendleft(): 왼쪽 끝에 0 추가
dq.appendleft(0)
print(f"appendleft(0) 후: {dq}")
# appendleft(0) 후: deque([0, 10, 20, 30, 40])

# 3. pop(): 오른쪽 끝 요소(40) 꺼내기
right_item = dq.pop()
print(f"pop()으로 꺼낸 값: {right_item}")
print(f"pop() 후: {dq}")
# pop()으로 꺼낸 값: 40
# pop() 후: deque([0, 10, 20, 30])

# 4. popleft(): 왼쪽 끝 요소(0) 꺼내기
left_item = dq.popleft()
print(f"popleft()로 꺼낸 값: {left_item}")
print(f"popleft() 후: {dq}")
# popleft()으로 꺼낸 값: 0
# popleft() 후: deque([10, 20, 30])
