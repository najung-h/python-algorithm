# --- 한계점 확인 예시 코드 ---
print("\n--- 2. 'False Full' 한계점 확인 ---")
queue = Queue(4)  # 용량이 4인 큐 생성

# 1. 큐를 가득 채움
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(f"큐가 가득 찼나요? {queue.is_full()}")  # True
print(f"큐 내부 리스트 상태: {queue.items}")  # [1, 2, 3, 4]
print(f"front: {queue.front}, rear: {queue.rear}\n")  # front: -1, rear: 3

# 2. 큐에서 데이터 2개를 꺼냄
queue.dequeue()
queue.dequeue()
print(f"큐의 현재 크기: {queue.get_size()}")  # 2
print(
    f"큐가 가득 찼나요? {queue.is_full()}"
)  # True (rear가 끝에 있어 여전히 Full)
print(f"큐 내부 리스트 상태: {queue.items}")  # [None, None, 3, 4]
print(f"front: {queue.front}, rear: {queue.rear}\n")  # front: 1, rear: 3

# 3. 새로운 데이터 추가 시도
# 큐에 2칸이나 비어있지만, rear가 배열 끝에 도달하여 더 이상 enqueue 할 수 없습니다.
queue.enqueue(5)  # IndexError: Queue is full
