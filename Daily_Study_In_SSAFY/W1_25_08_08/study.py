# 버블 정렬

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


numbers = [64,13,5,6,7,0,1,35476,456778,23452]
print("1. 버블 정렬 후:", bubble_sort(numbers))

# counting 정렬
arr = [0, 4, 1, 3, 1, 2, 4, 1]

def counting_sort(input_arr, k):
    '''카운팅 정렬 함수
    input_arr : 정렬할 입력 배열
    k : 입력 배열 내 원소의 최댓값
    '''

    # 1. 카운팅 배열
    counting_arr = [0] * (k+1)

    for num in input_arr:
        counting_arr[num] += 1
    
    #print(counting_arr)

    # 2. 누적합 배열
    for i in range(1, k+1):
        counting_arr[i] += counting_arr[i-1]

    # 3. 결과 배열
    result_arr = [0] * len(input_arr)

    for num in reversed(input_arr):
        counting_arr[num] -= 1
        result_arr[counting_arr[num]]  = num

    return result_arr


print('2. 카운팅 정렬 결과 : ', counting_sort(arr, 4))

# 델타 이동
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r, c = 1, 1  # 기준점
N, M = 3, 3

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
storage_lst = []

for i in range(4):
    for k in range(1, 3): # 범위
        nr = r + dr[i] * k
        nc = c + dc[i] * k

        if 0 <= nr < N and 0 <= nc < M:
            storage_lst.append(arr[nr][nc])

    # 이 아래는 모두 유효한 좌표임이 보장됨
print('* 델타이동에서, 델타이동한 좌표의 값은', storage_lst)

'''
# 8방향 델타: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
'''


# 이진 검색
def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left<= right:
        mid = (left + right) //2
        
        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:  # 왼쪽 탐색
            right = mid - 1

        else:                    # 오른쪽 탐색
            left = mid + 1

    return -1 # 검색 실패

numbers = [2, 4, 7, 9, 11, 19, 23]
print(f"3. 이진 검색 결과, '11'은 인덱스 {binary_search(numbers, 11)}에 있습니다.") # '11'은 인덱스 4에 있습니다.


# 셀렉션 알고리즘
def select(arr, k):
    '''
    주어진 리스트 arr에서 k번째로 작은 원소를 반환하는 함수
    '''
    for i in range(k):  # k 번만 정렬하면 됨
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr[k-1]

nums = [7, 5, 9, 1, 3, 10, 2]
k = 3  # 3번째로 작은 원소
print(f"4. 셀력선 알고리즘 결과, {k}번째로 작은 원소는:", select(nums, k))


