# 큐

0. 큐란, 먼저 들어온 데이터가 먼저 나가는 선형 자료구조입니다.



​	큐의 가장 명확한 특징은 

​	`선입선출(FIFO)` 인데요. 

​	가장 먼저 넣은 자료가 가장 먼저 나온다는 것입니다.



​	음식점에서 예약 대기 걸 때,

​	나보다 늦게 간 사람이 먼저 들어가는 일은 있을 수가 없겠죠

​	그런 거 생각해보시면 되겠습니다.



​	큐의 구조를 이제 보시겠습니다.

​	삭제 <- [ ㅇ ㅇ ㅇ ... ㅇ ㅇ ] <- 삽입

​	이처럼, 뒤에서는 삽입만 앞에서는 삭제만 이루어지는 구조로 생겼습니다



​	특히, **저장된 원소 중에 맨 앞 원소의 바로 앞 위치**를 `Front` 라고 하고,

​	**저장된 원소 중에 마지막 원소**를 `Rear` 이라고 합니다.



​	이런 큐의 기본 연산으로는

​	`enqueue(item)` : 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산

​	`dequeue()` : 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산

​	`create_queue()` : 공백 상태의 큐를 생성하는 연산

​	`is_empty()` : 큐가 공백상태인지를 확인하는 연산

​	`is_full()` : 큐가 포화상태인

​	`qpeek()` : 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산



​	qpeek은 "앞에 뭐가 있나 들여다보기"입니다.

​	큐의 원소를 삭제 / 삽입 / 반환 하지 않아요

​	"현재 가장 먼저 처리될 원소가 뭘까? == 웨이팅 1번이 누구야?" 확인할 때 사용합니다.

​	

​	선형 큐에서는, 

​	**시작시** front = rear = -1

​	**원소 삽입시** front 그대로, rear 오른쪽으로 한 칸 이동

​	**원소 반환 및 삭제시 ** rear 그대로, front만 오른쪽으로 한 칸 이동

​	반복하다가 front의 위치와 rear의 위치가 같아지면 **빈 큐**

​	반복하다가 rear의 인덱스가 capacity-1 에 위치하면 **가득찬 큐**가 됩니다.



​	근데, 선형 큐가 뭐냐고요?

​	선형 큐(Linear Queue)란, 

​	데이터를 일렬로 저장하며, 앞에서 꺼내고 뒤에 넣는 기본 큐 구조입니다.

​	

​	구현함에 있어,

​	아래 내용을 우선적으로 이해한다면 도움이 될 것입니다.



​	front : 가장 최근에 삭제된 원소의 인덱스  ** front는 원소를 삭제할 때만 이동됨*

​	rear : 마지막으로 저장된 원소의 인덱스 ** rear은 원소를 삽입할 때만 이동됨*

​	

​	초기상태 : front = rear =-1

​	공백상태 : front == rear

​	포화상태 : rear == n-1          (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

​	

​	그럼, 이제 구현해보시겠습니다.



##  선형 큐의 구현

```python
class Queue:
    def __init__(self, capacity=10):
        # 큐의 최대 크기
        self.capacity = capacity
        # 데이터를 저장할 리스트(None으로 채워둠)
        self.items = [None] * capacity
        # front는 맨 앞 요소 '바로 앞' 인덱스를 가리킴
        self.front = -1
        #rear는 마지막 요소의 인덱스를 가리킴
        self.rear = -1
        ### 즉, [None, 1, 2 ]라는 큐에서
        ### front는 0, rear는 2가 되는 것. 
        ### capacity는 3
        ### is_full == True


    def is_empty(self):
        # front와 rear가 같으면 큐가 비어있음
        return self.front == self.rear


    def is_full(self):
        # rear(인덱스값)가 capacity(개수) -1 에 도달하면 큐가 가득 찼다.
        return self.rear == self.capacity -1
    

    def enqueue(self, item):
        # 삽입하기 전에 가득 찼는지 확인
        if self.is_full():
            raise IndexError('큐가 가득 찼습니다.') # 에러를 발생시키고 싶은 곳에 raise
        self.rear += 1
        self.items[self.rear] = item


    def dequeue(self):
        # 삭제 전에 큐가 비었는지를 확인
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        # front 인덱스를 1 증가
        self.front += 1
        # front가 위치한 항목을 우선 변수에 담아두기
        item = self.items[self.front]
        # 해당 위치를 None으로 변경(제거)
        self.items[self.front] = None
        return item # front가 이동한 위치에 있는 기존 데이터 반환


    def peek(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        # 현재 큐의 맨 앞 요소를 반환
        return self.items[self.front + 1]

    def get_size(self):
        # rear에서 front값을 빼면 개수가 나온다.
        # [None, 1, 2]
        # 라는 큐에서, front(0), rear(2)임을 생각해보면 알 수 있다.
        return self.rear - self.front





# --- 기본 동작 예시 코드 ---
print("--- 1. 기본 동작 확인 ---")
queue = Queue(5)  # 용량이 5인 큐 생성

# 1. Enqueue (데이터 삽입)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"큐의 현재 크기: {queue.get_size()}")  # 3
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 10
print(f"큐 내부 리스트 상태: {queue.items}\n")  # [10, 20, 30, None, None]

# 2. Dequeue (데이터 추출)
# 가장 먼저 넣은 10이 가장 먼저 나옴 (FIFO)
print(f"Dequeue: {queue.dequeue()}")  # 10
print(f"큐의 현재 크기: {queue.get_size()}")  # 2
print(f"큐의 맨 앞 데이터 확인(peek): {queue.peek()}")  # 20
print(f"큐 내부 리스트 상태: {queue.items}")  # [None, 20, 30, None, None]


```



​	그러나, 선형 큐는 한계가 분명히 존재하는데,

​	"공간 재활용이 어렵다"는 것입니다.

​	"`False Full`" 이라는 개념으로 이야기하기도 하고요.



​	`	enqueue` / `dequeue`를 반복하다보면, 

​	front가 계속해서 증가하고,

​	앞쪽에 아무리 많은 빈 공간이 있어도

​	[None, None, 2]처럼

​	원소가 끝까지 채워졌으면 `is_full == True`, 

​	즉 못 쓰는 상태가 되어버려요.



​	이런 한계를 극복할 수 있는 개념이 바로, 

​	원형 큐 !



​	원형 큐의 경우, 선형큐와 본질적으로 다른 존재는 아니고,

​	선형 큐를 왼쪽 오른쪽 악력기 구부리듯이 구부려서

​	머리가 꼬리를 무는 꼬리물기 큐가 되었다고 생각하면 됩니다.



​	1차원 배열을 사용하되, 논리적으로는

​	배열의 처음과 끝이 연결되어

​	원형 형태의 큐를 이룬다고 가정하고 사용하는 것이죠



​	비유하면, 

​	[1시 2시 ... 11시 12시]의 선형큐를 구부려서

​	[    12시

​	  11시   1시

​	10시       2시]

​	이렇게 시계처럼 물고 물어지는 원형 큐를 만드는 것과 똑같다.. 입니다



​	그래서, 원형 큐는 

​	한정된 메모리 공간을 재활용하는 매우 효율적인 자료 구조를 가지는데요.	

---



​	이제, 원형 큐를 본격적으로 볼까요

​	

​	우선, 원형 큐(Circular Queue)란,

​	선형 큐의 공간 낭비를 막기 위해 처음과 끝이 연결된 구조입니다.

​	

​	원형 큐의 구조는 다음과 같습니다.

	- 초기 공백 상태 : front = rear = 0
	- index의 순환



​	원형 큐에 있어, 시계처럼, 6시 -> ... 12시 -> 1시 -> ... -> 12시 의 순환구조는

​	`모듈러 ( % ) 연산`을 이용해서 만듭니다



​	삽입연산을

​	선형큐에서는 rear +1 에 진행했다면

​	원형 큐에서는 rear +1 (mod n)으로 진행해요

​	즉, `rear = (rear + 1) % capacity`



​	삭제연산을

​	선형큐에서는 front + 1 에 진행했다면

​	원형 큐에서는 front + 1 (mod n)으로 진행해요

​	즉, `front = (front + 1) % capacity`



- front 변수

  공백 상태와 포화 상태 구분을 쉽게 하기 위해서 front가 있는 자리는 사용하지 않고요, 항상 빈자리로 냅둡니다.



​	<- 왜일까요?

​	 `rear`랑 `front`가 같으면 빈 큐인데,

​	그런 논리적 오류를 범하지 않기 위해서입니다.



​	다시 말해,

​	큐가 완전히 비어있는 상태와

​	가득 차있는 상태 모두에서,

​	`front`와 `rear`포인터가 같은 위치를 가리키게 되어

​	구분이 모호해지는 문제가 발생할 수 있는데요

​	이를 예방하기 위함입니다.



​	또한, 이렇게 원형 큐의 한 공간을 의도적으로 비워놓아야하기 때문에

​	`N`개의 데이터를 저장하고 싶다면, 실제 배열의 크기는 `N+1`로 만들어야겠죠.



​	그렇게 함으로써, empty 상태와 full 상태를 명확하게 구분할 수 있겠습니다.

​	즉, 

	- empty 상태 : `front == rear`  : front 와 rear 포인터가 같은 위치를 가리킬 때
	-  full 상태 : `(rear + 1) % capacity == front`  : rear 포인터의 바로 다음 위치가 front일 때



​	근데, 여기서 한 번 헷갈리실 수도 있어서 다시 보충 설명을 해볼게요.

​	우리 `front`는 맨 앞 원소의 바로 앞 칸을 가리킨다고 했죠

​	즉, **여기까지는 이미 꺼낸 자리다**라고 알려주는 역할이에요



​	반면에 `rear`은 마지막 원소가 들어 있는 칸을 가리킨다고 했죠

​	즉, **여기까지는 원소가 채워져있어**라고 표시하는 역할을 해요



​	그래서,

​	만약에 `front == rear`이라면

​	"엥, 방금 막 지운애가 front 자리앤데, 마지막으로 채운 애가 rear자리에 있었었어? 뭐야 다 지웠네??" 
​	라는 얘기니까 empty인 거에요

​	

​	만약에 `rear + 1 == front`라면

	[D, None, B, C]
	front=1, rear=0

​	rear가 더 이상 증가할 곳이 없어요.

​	즉, 원소를 삽입할 공간이 없다는 얘기죠

​	""



이제 코드를 구현 해볼게요.



### 원형 큐의 구현

```python
class CircularQueue:
    """
    고정 크기 리스트를 사용하여 원형 큐를 구현한 클래스입니다.
    front와 rear 포인터를 이용해 삽입과 삭제 연산을 O(1) 시간 복잡도로 수행합니다.
    """

    def __init__(self, capacity):
        """
        큐를 초기화합니다.
        capacity: 큐에 저장할 수 있는 최대 원소의 수
        """
        # [핵심] 큐가 비어있는 상태(front == rear)와 가득 찬 상태를 구분하기 위해
        # 요청된 용량(capacity)보다 1 크게 실제 리스트를 생성합니다.
        self.capacity = capacity + 1
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0
        # 원형 큐에서는 어차피 순환을 하기 때문에
        # 초기값이 굳이 0이 아니어도 사실 상관은 없다.


    def is_empty(self):
        """큐가 비어있는지 확인합니다."""
        # front와 rear 포인터가 같은 위치를 가리키면 큐는 비어있습니다.
        return self.front == self.rear


    def is_full(self):
        """큐가 가득 찼는지 확인합니다."""
        # rear 포인터의 다음 위치가 front와 같다면, 큐는 가득 찬 것입니다.
        # 모듈러(%) 연산을 통해 리스트의 끝과 처음이 연결된 것처럼 동작합니다.
        return (self.rear + 1) % self.capacity == self.front


    def enqueue(self, item):
        """큐의 맨 뒤(rear)에 데이터를 추가합니다."""
        # rear가 시계방향으로 한 칸 이동합니다.
        if self.is_full():
            # is_full()이 True이면, 예외를 발생시켜 프로그램에 오류를 알립니다.
            raise IndexError("Queue is full")

        # rear 포인터를 시계방향으로 한 칸 이동시킵니다.
        self.rear = (self.rear +1 ) % self.capacity
        # 새로운 rear 위치에 데이터를 삽입합니다.
        self.items[self.rear] = item
        

    def dequeue(self):
        """큐의 맨 앞(front)에서 데이터를 꺼냅니다."""
        # front 가 시계방향으로 한 칸 이동합니다.
        if self.is_empty():
            # 큐가 비어있으면 꺼낼 데이터가 없으므로 예외를 발생시킵니다.
            raise IndexError("Queue is empty")

        # front 포인터를 시계방향으로 한 칸 이동시켜, 가장 오래된 데이터를 가리키게 합니다.
        self.front = (self.front + 1) % self.capacity
        # 해당 위치의 데이터를 item 변수에 저장합니다.
        item = self.items[self.front]
        # (선택사항) 해당 위치의 데이터를 None으로 초기화하여 메모리를 관리합니다.
        self.items[self.front] = None
        ''' 왜 선택사항인거냐면,
         원형 큐는 관리되는 방식이 front와 rear포인터를 보고, 
         "여기가 비었네" "여기가 차있네" 관리하는 거잖아요

         그래서, dequeue할 때 실제 데이터를 None으로 지우지 않아도, 
         포인터 위치만으로 큐의 상태를 관리할 수 있어요

         그럼에도 불구하고, 왜 초기화를 해주냐.
         메모리 관리 측면에서 그렇습니다.
         그리고 하나 더, print(queue.items)로 찍어봤을 대
         이미 제거된 자리들이 None으로 표시되면 눈으로 확인하기 쉬워서
         디버깅 측면에서의 이점이 있습니다.
         '''
        # 저장해 둔 데이터를 반환합니다.
        return item

    def peek(self):
        """큐의 맨 앞에 있는 데이터를 삭제하지 않고 확인합니다."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        # front의 '다음' 위치가 큐의 실제 시작점이므로, 해당 위치의 항목을 반환합니다.
        return self.items[(self.front + 1) % self.capacity]


    def get_size(self):
        """현재 큐에 저장된 데이터의 개수를 반환합니다."""
        # rear가 front보다 뒤에 있을 때(일반적인 경우): rear - front
        # rear가 front보다 앞에 있을 때(순환한 경우): rear - front + capacity
        # 이 두 경우를 모듈러 연산을 통해 하나의 식으로 처리할 수 있습니다.
        return (self.rear - self.front + self.capacity) % self.capacity 
        ''' 근데 self.capacity는 굳이 안 더해줘도 되는 거 아냐? 왜 더 해야해?
        라는 질문에 대해서 gpt한테 물어보니,
        파이썬 한정 상관없다.
        그러나, 언어 불문하고 안전하게 쓰려면 self.capacity를 더해주는 게 맞다. 라고 한다.

        "(GPT) 파이썬에선 음수 나머지가 항상 0 이상이므로
        return (self.rear - self.front) % self.capacity 만으로 충분히 정확합니다.

        + self.capacity는 타 언어 호환/교육용 명시성 때문에 붙이는 관용입니다. 
        (C/Java에선 음수 %가 음수가 될 수 있음"

        '''


queue = CircularQueue(3)   # 실제 저장 가능 개수 = 3, 내부 리스트 크기 = 4 짜리인 큐를 만들자
queue.enqueue('A')
queue.enqueue('B')
print(queue.dequeue())  # A

queue.enqueue('C')
queue.enqueue('D')
print(queue.items)  # ['D', None, 'B', 'C']
print(queue.get_size())  # 3

queue.enqueue('Z')  # IndexError: Queue is full

```



위와 같은 원형 큐는 

1) 공간 효율성

2) 속도(O(1))측면에서 이점이 있습니다.

   (연산이 모두 포인터 이동으로만 이루어지므로, 큐의 크기와 상관없이 항상 빠른 속도가 보장됩니다.)



이러한 원형 큐는 

1. BFS(미로찾기, 최단경로문제) 등에서, 거의 공식처럼 사용됩니다.
2. 프린터 인쇄 대기열





마지막으로 

### deque

도 한 번 보겠습니다.



위에서 원리를 잘 이해했다면

이제는 deque로 편리하고 빠르고 간단하게 구현하시면 됩니다.

```python
from collections import deque

# deque 객체 생성
queue = deque()

# 1, 2, 3을 차례로 큐에 삽입 (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)

# 큐에서 세 개의 데이터를 차례로 꺼내서 출력 (dequeue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
```















