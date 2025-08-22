# 수식트리 Expression Tree 
# 피연산자는 반드시 리프에 있어야한다.
# 연산자는 반드시 루트 노드 또는 가지 노드에 위치해야한다.


import sys

sys.stdin = open('expression_input.txt')


# 후위 순회를 이용해 수식을 계산하는 재귀 함수
def calc(node_index):
    """
    node_index: 현재 계산할 노드의 번호
    """
    # --- 기저 조건 (Base Case) ---
    # 재귀의 탈출 조건으로, 현재 노드가 더 이상 계산할 자식이 없는
    # 리프 노드(피연산자, 즉 숫자)일 때를 의미합니다.
    
    # 이 문제의 입력 형식상, 리프 노드는 ['노드번호', '값'] 형태로
    # 길이가 2이므로, len()을 통해 리프 노드 여부를 판별할 수 있습니다.
    if len(tree_info[node_index]) == 2:
        # 현재 노드가 가진 숫자 값을 정수로 변환하여 반환합니다.
        # 이 반환 값은 부모 노드의 연산에 사용될 '피연산자'가 됩니다.
        return int(tree_info[node_index][1])

    # 재귀 호출(Recursive Step): 정보 길이가 2가 아니면 연산자 노드
    else:
        # 왼쪽 자식과 오른쪽 자식의 인덱스를 가져옴
        left_child_idx = int(tree_info[node_index][2])
        right_child_idx = int(tree_info[node_index][3])

        # 각각의 자식 노드로 재귀 호출하여 하위 트리의 계산 결과를 얻음
        left_val = calc(left_child_idx)
        right_val = calc(right_child_idx)

        # 현재 노드의 연산자로 두 결과를 계산하여 반환
        op = tree_info[node_index][1]
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        else:  # '/'
            # 문제 조건에 따라 정수 나눗셈으로 처리
            return left_val // right_val


# --- 메인 로직 ---
N = int(input())  # 노드의 총 수

# 각 노드의 원본 입력 정보를 그대로 저장할 리스트
# 1번 노드부터 사용하기 위해 0번 인덱스는 비워둠
tree_info = [[] for _ in range(N + 1)]
for _ in range(N):
    # 입력 예: ['1', '-', '2', '3']
    node_input = input().split()
    # 노드 번호를 인덱스로 사용하여 정보 저장
    tree_info[int(node_input[0])] = node_input
    """
    만들어진 tree_info
    [[], ['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10'], ['4', '88'], ['5', '65']]
    """

# 루트 노드(1번)부터 계산 시작
result = calc(1)

print(f'{result}')
