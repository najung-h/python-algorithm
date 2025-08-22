import sys

sys.stdin = open('input.txt')


# 전위 순회(Preorder Traversal)
# 루트 노드를 먼저 방문하고, 왼쪽 자식 노드를 방문하고, 오른쪽 자식 노드를 방문하는 순서
def preorder(node):
    # node가 0이 아닐 때만(유효한 노드일 때만) 실행
    if node != 0:   # 재귀함수에 있어, 탐색을 종료하는 지점.
        # 1. 나 먼저 처리 (V)
        print(node, end=' ')
        # 2. 왼쪽 자식으로 이동 (L)
        preorder(left[node])
        # 3. 오른쪽 자식으로 이동 (R)
        preorder(right[node])


V = int(input())
E = V - 1

left = [0] * (V + 1)
right = [0] * (V + 1)

edge = list(map(int, input().split()))

for i in range(E):
    parent, child = edge[i * 2], edge[i * 2 + 1]

    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

root = 1
preorder(root)
