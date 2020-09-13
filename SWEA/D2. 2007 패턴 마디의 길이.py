T = int(input())
for test_case in range(1, T + 1):
    string = input()
    findNode = 0
    
    for i in range(0, 11):
        for j in range(1+i, 11+i):
            if string[i] == string[j]:
            	if findNode < j - i:
                    findNode = j - i
            	break
    print(f'#{test_case} {findNode}')