def comb(arr, r):
    """
    Args:
        arr (list): 원본 배열
        r (int): 뽑을 개수

    Returns:
        list: 모든 조합이 담긴 2차원 리스트
    """
    result = []

    # 기저 조건(Base Case): 뽑을 개수가 0이면, 빈 리스트를 담은 리스트를 반환하여 조합 완성
    if r == 0:
        return [[]]
        '''
        - 조합에서는 "더 이상 뽑을 원소가 없을 때 (`r == 0`)"가 바로 그 탈출 신호입니다.
	    - `[[]]`를 반환하는 이유는 "조합 하나를 완성했으니, 여기에 네가 지금까지 고른 원소들을 합쳐라"는 신호를 보내기 위함입니다.
        '''
    # 재귀 호출(Recursive Step)
    for i in range(len(arr)):
        # i번째 원소를 첫 번째 요소로 선택
        '''for 루프는 "이번 조합에 첫 번째로 포함시킬 원소"를 모든 경우에 대해 한번씩 시도하는 과정입니다. i=0일 때는 1을, i=1일 때는 2를 첫 번째 원소로 선택하는 세계관으로 들어갑니다.'''
        elem = arr[i]

        # i번째 원소 이후의 나머지 리스트에서
        # 나머지 (r-1)개의 조합을 재귀적으로 구함
        for rest in comb(arr[i + 1 :], r - 1):
            # 선택한 요소(elem)와 나머지 조합(rest)을 합쳐 결과에 추가
            result.append([elem] + rest)

    return result


# --- 실행 코드 ---
all_combs = comb([1, 2, 3, 4], 3)
print(all_combs)

# [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]