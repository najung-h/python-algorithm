def counting_sort(input_arr, k):

    # 각 원소의 개수를 카운트하여 저장할 lst를 생성합니다.
    # input_array를 순한하며, 해당 정수값을 인덱스로 삼아
    # count_lst[인덱스]에 값을 +1씩 예정입니다.

    ## 1. 리스트 생성
    count_lst = [0] * k

    ## 2. input_array를 순환하며 count_lst 완성하기

    for i in input_arr:
        count_lst[i] += 1
    
    ### 이렇게
    ### print(count_lst) 
    ### [1, 3, 1, 1, 2]

    # 이제 누적합 count lst로 바꿔줍니다.
    # count_lst를 앞에서부터 순환하며,
    # 바로 직전 원소값과 자신을 더한 값을
    # 내 위치에 다시 저장하도록 하겠습니다.

    # 3. 누적 리스트 생성
    for idx in range(1, len(count_lst)):
        count_lst[idx]  += count_lst[idx -1]
    
    # print(count_lst)
    # [1, 4, 5, 6, 8]


    # 이제, 결과 lst를 생성합니다. 
    # input_array를 역순으로 이동하며
    # 결과 array에 한땀한땀 숫자를 집어넣어주겠습니다.

    ## 4.  결과 리스트 생성
    ### 길이는 input_lst랑 똑같게 맞춰줍니다.
    result_lst = [0] * len(input_arr)


    ## 5. 역순으로 결과 리스트에 한땀한땀 입력해주기
    for i in input_arr[::-1]:      ### 역순으로  ### reversed(input_arr) 함수로도 가능
        count_lst[i] -= 1          ### 누적합에서 하나 빼주고,
        idx = count_lst[i]         ### 그 값을 idx로 받아와서
        result_lst[idx] = i        ### 그걸을 인덱스 삼아. i를 입력해주겠습니다.

    return result_lst
    
    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
k = max(arr) +1
print('정렬 결과:', counting_sort(arr, k))  # [0, 1, 1, 1, 2, 3, 4, 4]