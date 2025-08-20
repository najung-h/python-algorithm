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
