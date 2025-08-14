def bubble_sort(arr):
    replace = False

    while replace is False:
        # 재귀함수로다가 만들어줄 예정입니다.

        # 매번 replace를 fale로 설정하고 시작합니다.
        # 만약 반복문을 돌면서, 한 번도 순서를 뒤집지 않았다면
        # replace = False로 남아있을텐데
        # 그 리스트는 잘 정렬된 것이므로
        # 반복문을 끝내고, sorted_numbers를 리턴할 것입니당

        replace = False

        len_number = len(numbers)
        for n in range(len_number-1):
            num2 = int(numbers[-n-1])
            num1 = int(numbers[-n-2])
            if num2 < num1:
                replace = True
                numbers[-n-1], numbers[-n-2] = numbers[-n-2], numbers[-n-1]

        # 반복문이 다 끝났는데 replace is False라면:
        if replace is False:  # 싱글턴은 is 로 비교
            sorted_numbers = numbers
            return sorted_numbers
        else:
            replace = False


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)