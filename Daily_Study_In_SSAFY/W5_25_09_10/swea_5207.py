import sys
sys.stdin = open('input_5207.txt', 'r')



def binary_search_recursive(target, left_idx, right_idx, direction):
    """
    target: 찾으려는 값
    left_idx, right_idx: 현재 탐색 범위, 시작점과 출발점
    direction: 직전 탐색에서 이동한 방향 ('LEFT', 'RIGHT', 'START')
    """
    global cnt

    # [종료 조건] 탐색 범위가 유효하지 않으면 실패입니다.
    if left_idx > right_idx:
        return

    mid = (left_idx + right_idx) // 2

    # 목표 값을 찾았다면, 카운트를 1 증가시키고 탐색을 종료합니다.
    if A[mid] == target:
        cnt += 1
        return

    # 목표 값이 중앙값보다 작아 왼쪽 구간을 탐색해야 하는 경우
    elif A[mid] > target:
        # 직전 탐색 방향이 'LEFT'였다면 규칙 위반이므로 탐색을 중단합니다.
        if direction == 'LEFT':
            return
        # 왼쪽으로 탐색을 진행하고, 방향을 'LEFT'로 기록하여 재귀 호출합니다.
        binary_search_recursive(target, left_idx, mid - 1, 'LEFT')

    # 목표 값이 중앙값보다 커 오른쪽 구간을 탐색해야 하는 경우
    else:  # A[mid] < target
        # 직전 탐색 방향이 'RIGHT'였다면 규칙 위반이므로 탐색을 중단합니다.
        if direction == 'RIGHT':
            return
        # 오른쪽으로 탐색을 진행하고, 방향을 'RIGHT'로 기록하여 재귀 호출합니다.
        binary_search_recursive(target, mid + 1, right_idx, 'RIGHT')



T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # A는 정렬해둬야함.
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    arr = A+B

    # b에 저장된 원소에 대해 a에 들어있는 원소인지 확인한다.
    # 카운트 초기화
    cnt = 0

    for integer in B:
        # 처음 탐색은 중립 방향('START')에서 시작합니다.
        binary_search_recursive(integer, 0, N-1, 'START')
        

    print(f'#{tc} {cnt}')