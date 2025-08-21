def perm(selected, remaining):
    """
    Args:
        selected (list): 현재까지 선택된 원소들의 순열 (선택된)
        remaining (list): 아직 선택되지 않은 원소들 (선택할)
    """
    # 기저 조건(Base Case): 더 이상 선택할 원소가 없으면 순열 하나가 완성된 것
    if not remaining:
        print(selected)
        return

    # 재귀 호출(Recursive Step)
    # 남아있는 원소들(remaining)을 하나씩 순회하며 다음 자리에 놓을 원소를 선택
    for i in range(len(remaining)):
        # i번째 원소를 이번 순열에 추가
        pick = remaining[i]

        # i번째 원소를 제외한 새로운 '남은 원소' 리스트 생성
        new_remaining = remaining[:i] + remaining[i + 1 :]

        # 새로운 '선택된 원소'와 '남은 원소'로 자기 자신을 다시 호출
        perm(selected + [pick], new_remaining)


# --- 실행 코드 ---
# 처음에는 아무것도 선택되지 않았고([]), 모든 원소가 남아있음([1, 2, 3])
perm([], [1, 2, 3])

'''
<output>
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''