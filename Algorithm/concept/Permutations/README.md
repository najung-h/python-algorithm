# 순열

[python 공식 문서_itertools](https://docs.python.org/ko/3.9/library/itertools.html)



순열이란, 

주어진 원소들을 **순서 있게** 나열하는 것을 의미합니다.

** 순서가 중요합니다



고등학교 때 배우셨을 테니, 

자세한 설명은 생략하겠습니다.



`nPr` : 전체 원소가 n개 있을 때, r개를 뽑아 순서 배열하는 경우

```markdown
nPr = n * (n - 1) * (n - 2) * ... * (n - r + 1)
    = n! / (n-r)!
```

 ** 모든 원소(n개)를 다 쓰는 순열은 npn이 되며, 이는 `n!`와 동일합니다.

** 참고로, `nP0`은 1입니다.



---



그래서, 어떻게 구현되냐면요

1. 반복문 방식

   ```python
   # {1, 2, 3}의 모든 순열을 구하기 위한 3중 for문
   
   for i in range(1, 4):
       for j in range(1, 4):
           # i와 j가 겹치지 않는 경우에만 다음 단계로
           if i != j:
               for k in range(1, 4):
                   # i, j, k가 모두 겹치지 않는 경우 출력
                   if i != k and j != k:
                       print(i, j, k)
   
   
   '''
   output
   
   1 2 3
   1 3 2
   2 1 3
   2 3 1
   3 1 2
   3 2 1
   
   '''
   ```

   한계가 한 번에 딱 봐도 명확하죠

   지금은 원소 3개라 3중 for 문이지만

   원소가 n개가 되면 n중 for문을 제작해야합니다.

   10 개 면 10중 for문... 가능하시겠어요?

   

2. 재귀방식

   위와 같은 한계를 극복하기 위해 재귀로 만듭니다.

   ```python
   def permutation(arr, r):
       for i in range(len(arr)):
           if r == 1:
               yield (arr[i],)
           else:
               for next in permutation(arr[:i] + arr[i+1:], r-1):
                   yield (arr[i],) + next
   
   
   arr = [1,2,3]
   print(list(permutation(arr, 2)))
   
   # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
   ```

   

​	제가 이해 과정에서 참고했던 코드도 함께 공유드립니다.

​	핵심 로직은, 

​	현재 요소를 포함시킬지 결정하고, 나머지 요소들로 나머지 개수를 채우는 재귀적 구조라고 보시면 됩니다.

```python
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
```



# 파이썬에서 실질적 구현

그런데, 파이썬에서는 permutation을 쉽사리 구현하실 수 있습니다.

물론, 코딩테스트에서 itertools를 제한시켜놓을 수 있으니,

직접 구현하는 def 버전도 외우시긴 해야합니다.

```python
import itertools

arr = [1, 2, 3, 4]

print(list(itertools.permutations(arr, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), 
#        (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]



from itertools import permutations

arr = [1, 2, 3, 4]

print(list(permutations(arr, 2)))
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), 
#       (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

```



** 주의 사항을 추가로 안내드립니다.

`itertools.permutations(iterable, r=None)`는 iterator를 반환합니다.

이는 generator와 마찬가지로, 일회용품 객체입니다.

즉, 한 번 순회가 끝나면 재사용이 불가합니다.

때문에, 필요한 경우, list() 또는 tuple() 로 먼저 형변환한 이후에 여러 번 재사용을 하셔야 합니다.













