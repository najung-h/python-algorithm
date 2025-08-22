'''축구를 하기 위해서 항상 짝수 N명이 모인다. '''


def score_in_the_team(team):
    score = 0
    comb_lst = list(combinations(team ,2 ))

    for idx, jdx in comb_lst:
        score +=  (S[idx][jdx] + S[jdx][idx])

    return score


from itertools import combinations

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

team  = list(combinations(range(N), N//2))
team_set = set(team)

A_team = [people for people in team if 0 in people]
A_team_set = set(A_team)  # 차집합 연산을 위한 형변환

min_diff = float('inf')

for A in A_team_set:
    B = list(set(range(N)) - set(A))

    A_score = score_in_the_team(A)
    B_score = score_in_the_team(B)

    diff = abs(A_score - B_score)

    if diff < min_diff : 
        min_diff = diff

    if diff == 0 : #최적값이라면
        min_diff = 0
        break

print(min_diff)



 
'''gpt의 조언

1) combinations는 이터레이터이므로 리스트로 변환하지 말고 바로 순회합니다.
2) `S[i][j] + S[j][i]`는 대칭적이므로 루프 외부에서 `pair_sum[i][j] (i<j)`로 미리 계산해두면 합산 연산량이 줄어듭니다.
        # 전
        comb_lst = list(combinations(team, 2))
        for a, b in comb_lst:
            score += (S[a][b] + S[b][a])

        # 후
        for a, b in combinations(team, 2):
            score += pair_sum[min(a,b)][max(a,b)]

3) `S`를 전역으로 참조하지 말고 함수 인자로 전달합니다.



'''