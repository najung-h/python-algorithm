arr = [1, 2, 3, 4]

# i: 0~2^n == i번째 부분집합
for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()

# 검사하고자 하는 비트를 오른쪽으로 하나씩 shift 하면서 체크하는 코드
def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(len(arr)):
        # 0x1 로 표기한 이유 (사실 1, 0b1, 0b0001, True 다 된다)
        # - 비트 연산임을 명시하는 권장 방법
        if tar & 0x1:  # 가장 우측 비트를 체크
            print(arr[i], end=' ')
        tar >>= 1


for target in range(1 << len(arr)):
    get_sub(target)
    print()