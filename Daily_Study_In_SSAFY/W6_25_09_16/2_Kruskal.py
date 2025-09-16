import sys
sys.stdin = open('mst_input.txt', 'r')


def find_set(x):
    '''대표자 찾기'''
    if x == parents[x]:
        return x

    # 자기 자신이 대표자가 아니래요
    # 그러면, 부모가 대표자일 수가 있으니까
    # 한 번 더 돌아가주는 게 기본 코드입니다.

    # 기본 코드
    # return find_set(parents([x]))

    # 그렇지만, 기본 코드는 너무 비효율적이기 때문에
    # 경로 압축까지 넣기로 했엇죠.

    # 경로 압축 코드
    find_set(parents[x]) # 대표자가 return
    # 현재 내가 바라보고 있는 부모를 대표자로 만들어주고
    parents[x] = find_set(parents[x])
    # 이 부모를 리턴해주자
    return parents[x]


def union(x ,y):
    '''x의 대표자와 y의 대표자를 꺼내서 병합해주기'''
    # 너네 먼저 대장 데리고 와
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry: # 사이클 발생
        return 

    # 발생하지 않았다면, 너 들어와라
    # 그런데, 조금 더 일정한 규칙을 위해서
    # 큰 애를 작은 애한테 편입시켜볼까

    # 일정한 규칙으로 병합 ( 더 작은 수로 )
    if rx < ry :
        parents[ry] = rx    
    else:
        parents[rx] = ry






V, E = map(int, input().split())


# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))  # 간선들의 정보를 저장

# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])
# print(edges)
# [(3, 5, 18), (1, 2, 21), (2, 6, 25), (0, 2, 31), (0, 1, 32), (3, 4, 34), (4, 5, 40), (2, 4, 46), (0, 6, 51), (4, 6, 51), (0, 5, 60)]


# 2. 가중치가 작은 간선부터 순서대로 선택하자
# - 사이클이 발생하면 고르지 말자!
# - 언제까지?
# - Mst가 완성될 때까지
# - == V-1개를 선택할 때까지

cnt = 0 #현재까지 선택한 간선의 수
result = 0 # 가중치의 합


'''
사이클 검증을 위해서는
union find code 사용하면 된다.

그리고, union find 에는 세 가지가 필요했다. 
    즉, 1. 집합 생성 2. 대표자 찾기 3. 병합'''
# make_set(집합 생성)
parents = [i for i in range(V)]
# find_set (대표자 찾기)
# union (병합)

for U, V, W in edges:
    '''
    1. 사이클 검증부터 : 사이클이 아니라면
        - 연결 (같은 집합으로 만든다)
    
            - cnt += 1
             - cnt 가 V-1 이라면 종료
    '''


    # 사이클 검증부터 : 사이클이 아니라면
    if find_set(U) != find_set(V):
        print(U, V, W)
        # - 연결 (같은 집합으로 만든다)
        union(U, V)
        cnt += 1
        result += W

        if cnt == V-1:
            break

print(f'최소 비용 = {result}')















