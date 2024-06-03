"""
정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 
경우의 수를 구하는 프로그램을 작성하세요 
예를 들어 1을 입력햇을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각 입니다.

00시 00분 03초 
00시 13분 30초
반면에 안세도 되는 시각은 
00시 02분 55초
01시 27분 45초

N = 5 , reutrn = 11475
"""
def solution(n):
    count = 0 
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h):
                    count +=1 
                elif "3" in str(m):
                    count +=1 
                elif '3' in str(s):
                    count +=1 

    return count 

print(solution(5))

"""
완전탐색문제 유형 

"""
# 이코테 
def solution2(n):
    count = 0 
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) +str(k):
                    count+=1 

    return count 

print(solution2(5))