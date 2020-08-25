T = int(input())
for test_case in range(1, T + 1):
    date = int(input())
    
    if date % 100 >= 32 or date % 100 == 0:		# 일이 0 또는 32 이상
        print(f'#{test_case} -1')
    elif date // 100 % 100 == 0 or date // 100 % 100 > 12:	# 월이 0 또는 12 초과
        print(f'#{test_case} -1')
    elif date % 10000 == 1131 or date % 10000 == 229 or date % 10000 == 230 or date % 10000 == 231 or date % 10000 == 431 or date % 10000 == 631 or date % 10000 == 931:
        # 예외: 2월 29, 30, 31일 / 4월 31일 / 6월 31일 / 9월 31일 / 11월 31일
    	print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {str(date // 10000).zfill(4)}/{str(date % 10000 // 100).zfill(2)}/{str(date % 100).zfill(2)}')