import sys

sys.stdin = open('input.txt')


# 후위 순회(Postorder Traversal)
# 왼쪽 자식 노드를 방문하고, 오른쪽 자식 노드를 방문하고, 루트 노드를 방문하는 순서
def postorder(node):
    if node != 0:
        # 1. 왼쪽 자식으로 이동 (L)
        postorder(left[node])
        # 2. 오른쪽 자식도 먼저 (R)
        postorder(right[node])
        # 3. 나는 맨 마지막에 처리 (V)
        print(node, end=' ')


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
postorder(root)
