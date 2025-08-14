import sys
sys.stdin = open('input_grading.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    correct_lst = list(map(int, input().split()))
    student_answer_lst = [list(map(int, input().split())) for _ in range(N)]


    score_lst = [] # 각 학생의 점수 기록

    for student in student_answer_lst:
        total_point = 0
        now_point = 0
        for q in range(M): # 각 문항에 대해
            if student[q] == correct_lst[q] : # 정답
                now_point += 1
                total_point += now_point
                #print(f'{q+1}번 맞았어요, {now_point}점 획득! 지금까지 총 {total_point}입니다')
            else: # 오답
                now_point = 0

        #print('채점 끝~ 고생했어요~')
        score_lst.append(total_point) # 각 학생마다 점수 기록
    


    print(f"#{test_case} { max(score_lst) - min(score_lst) }")


