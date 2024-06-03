"""
왕실의 나이트 문제 
행복 왕국의 왕실 정원은 체스판과 같은 8 * 8 좌표평면 입니다. 왕실 정원의 특정한 한 칸에 나이트가 있습니다. 
일반 체스의 나이트 처럼 움직인다. 

8*8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오 
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로, 열위치는 a~h로 표현 합니다. 

c2에 있을 때 이동할 수 있는 경우의 수는 6가지 입니다. 
a1에 있을 떄 경우의 수 2가지

"""
def solution(n):
    col = ["a",'b','c','d','e','f','g','h']
    row = ['1','2','3','4','5','6','7','8']
    count = 0 
    x = col.index(n[0])
    y= row.index(n[1])
    # x 
    xr=x+2 
    xl=x-2
    yr=y+2
    yl=y-2

    if xr < 8:
        if y + 1 < 8:
            count +=1 
        if y -1 >=0:
            count +=1
    if xl >= 0:
        if y +1 <8:
            count +=1 
        if y -1 >=0:
            count +=1 
    if yr < 8:
        if x +1 <8:
            count +=1 
        if x -1 >=0:
            count +=1 
    if yl >= 0 :
        if x + 1 <8:
            count +=1 
        if x -1 >=0:
            count +=1 

    return count


print(solution('c2'))
print(solution('a1'))

"""
요구사항대로 구현하면 되는 문제 
나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인합니다. 
"""
# 이코테 
def solution2(n):
    row= int(n[1])
    column = int(ord(n[0])) - int(ord('a')) + 1 # 아스키코드 

    steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인 
        next_row = row + step[0]
        next_column = column + step[1]

        if next_row >= 1 and next_row <=8 and next_column >=1 and next_column<=8:
            result +=1 
    return result 

print(solution2('c2'))
print(solution2('a1'))
