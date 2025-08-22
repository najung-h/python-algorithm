import sys

sys.stdin = open('input.txt')


# 중위 순회(Inorder Traversal)
# 왼쪽 자식 노드를 방문하고, 루트 노드를 방문하고, 오른쪽 자식 노드를 방문하는 순서
def inorder(node):
    if node != 0:
        # 1. 왼쪽 자식으로 이동 (L)
        inorder(left[node])
        # 2. 돌아와서 나 처리 (V)
        print(node, end=' ')
        # 3. 그 다음 오른쪽 자식 (R)
        inorder(right[node])


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
inorder(root)
