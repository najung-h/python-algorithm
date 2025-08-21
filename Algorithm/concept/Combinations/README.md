# 조합

[python 공식 문서_itertools](https://docs.python.org/ko/3.9/library/itertools.html)



조합은

**순서에 상관없이** 서로 다른 `n`개의 원소에서 `r`개를 선택하는 모든 경우의 수를 의미합니다.



조합의 경우의 수는

`nCr` = `n !   /   (r !  *  (n - r) !)`으로 구합니다.



---

구현해봅시다.

반복문으로 구현하면 아래와 같습니다.

```python
numbers = [1, 2, 3, 4]
n = len(numbers)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            print(numbers[i], numbers[j], numbers[k])
            
'''
<output>

1 2 3
1 2 4
1 3 4
2 3 4
'''
            
```

정의대로라면 

`if`문을 활용해서, i != j != k 임을 확인해야하지만,

아예 인덱스를 활용해서 같을 경우를 제거해버림으로써

순서가 다른 중복된 조합은 제거할 수 있습니다.



---



자, 이번에는 한 번 재귀 방식으로 구현해봅니다.

제가 애용하는 방식입니다.

```python
def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield (arr[i],)
        else:
            for next in combinations(arr[i + 1:], r - 1):
                yield (arr[i],) + next  


arr = [1, 2, 3]
print(list(combinations(arr, 2)))
# [(1, 2), (1, 3), (2, 3)]

```



다른 방식으로도 재귀문을 활용해볼 수 있습니다.

물론 논리는 똑같습니다.

```python
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
    # - 조합에서는 "더 이상 뽑을 원소가 없을 때 (`r == 0`)"가 바로 그 탈출 신호입니다.
	# - `[[]]`를 반환하는 이유는 "조합 하나를 완성했으니, 여기에 네가 지금까지 고른 원소들을 합쳐라"는 신호를 보내기 위함입니다.

    # 재귀 호출(Recursive Step)
    for i in range(len(arr)):
        # i번째 원소를 첫 번째 요소로 선택
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
```



그렇지만, 웬만한 경우에서는 itertools를 이용해

쉽사리 구현하면 되십니다.

```python
from itertools import combinations

arr = [1, 2, 3, 4, 5]

print(list(combinations(arr, 3)))
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
```



이상으로 조합의 내용은 마무리해볼게요.