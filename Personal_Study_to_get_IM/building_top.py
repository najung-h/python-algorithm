import sys
sys.stdin = open('input_building_top.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, W1, W2 = list(map(int, input().split()))
    weight_lst = list(map(int, input().split()))

    #무게 내림차순으로 정렬해주겠습니다.
    weight_lst = sorted(weight_lst, reverse=True)

    low_top_lst = [0] * min(W1, W2)
    #high_top_lst = [0] * max(W1, W2)
    high_top_lst = []


    for n in range(N):
        if n%2 ==1 and n //2+1 <= len(low_top_lst): # 작은 탑이 아직 안 채워졌다면
            low_top_lst[n//2] = weight_lst[n]
            weight_lst[n] = 0 # 채운 애는 없애버리고 싶은데, 인덱스는 유지해야하므로 0으로 초기화시켜

    # 이제 큰 탑 채우자 # 남은 애들은 다 1층부터 넣어
    for n in range(N):
        if weight_lst[n] != 0:
            high_top_lst.append(weight_lst[n])

    
    # 이제 탑의 층 수 * 화물을 해서 소요 비용을 구해볼까
    total_cost = 0

    for tdx in range(len(low_top_lst)):
        total_cost += low_top_lst[tdx] * (tdx+1)
    
    for tdx in range(len(high_top_lst)):
        total_cost += high_top_lst[tdx] * (tdx+1)


    print(f"#{test_case} {total_cost}")


