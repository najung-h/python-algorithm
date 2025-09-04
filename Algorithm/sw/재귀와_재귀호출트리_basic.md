재귀를 연습하기 전, 알아야 할 함수의 특징 1

1. int 같은 기본 타입은 함수에 넘길 때 값만 복사된다. 그래서 함수 안에서 바꿔도 원래 값은 안 바뀐다

   ```python
   ## 잘못 된 예
   def KFC(x):
       x += 1
   
   x = 3
   KFC(x)
   print(x)  # 3
   ```

   ```python
   ## 심화 이해
   def KFC(x):
       print(x) # 4
       x += 1
       print(x) # 5
   
   x = 3
   KFC(x + 1)
   print(x) # 3
   ```

2. 함수가 끝나면 해당 함수를 호출했던 곳으로 돌아옴

   ```python
   def BBQ(x):
       x += 10
       print(x) # 19
   
   def KFC(x):
       print(x) # 4
       x += 3
       BBQ(x + 2)
       print(x) # 7
   
   x = 3
   KFC(x + 1)
   print(x) # 3
   ```

   ```txt
   <출력>
   4
   19
   7
   3
   ```

---

#### 재귀 호출 트리는 for문 반복과 원리가 같다

1. 재귀 호출 트리

   ![재귀 호출 트리의 이미지 예시](C:\Users\SSAFY\Desktop\NJH_git\JH-studying-main\Daily_Study_In_SSAFY\W5_25_09_04\images\image-1.png)

   ```python
   ## 재귀로 구현하였을 때 
   
   def KFC(x):
       if x == 3:
           return
       
       KFC(x + 1)
       KFC(x + 1)
       KFC(x + 1)
       KFC(x + 1)
   
   KFC(0)
   
   # 반복문으로 구현하였을 때 
   def KFC(x):
       if x == 3:
           return
       for i in range(1,4):
           KFC(X+1)
   
   KFC(0)
   
   ```

   

- 종료조건 ( 기저조건 - Base Case )를 잘 설정해야 한다.
- 재귀호출과 stack이 밀접한 관련이 있다.





