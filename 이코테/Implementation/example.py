"""
상하좌우 문제 

여행가 A는 N X N 크기의 정사각형 공간 위에 서있습니다. 이 공간은 1X1크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 1,1 이며 가장 오른쪽 좌표는 (N,N) 입니다. 

여행가는 상하좌우 방향으로 이동할 수 있으며 시작 좌표는 항상 1,1 입니다. 
우리 앞에는 여행가가 이동할 계획이 적힌 계획서가 놓여 있습니다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 L R U D 중 하나의 문자가 반복적으로 적혀 있습니다. 
각 문자의 의미는 다음과 같습니다. 

L: 왼쪽으로 한 칸 
R : 오른쪽으로 한 칸 
U : 위로 한 칸 
D : 아래로 한 칸 

이 때 여행가는 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 

"""

def solution(data,n):
    left = (-1,0)
    right = (1,0)
    up = (0,-1)
    down = (0,1)

    location = (1,1)
    for i in data:
        i = i.upper()
        loc = location
        if i == "U": 
            loc = (loc[0]+up[0],loc[1]+up[1])
            print("up loc",loc)
            if loc[1] <= n and loc[1] > 0:
                location = loc
                print("play?")
            else:
                continue
        elif i == "D": 
            print("down pre loc",loc)
            loc  = (loc[0]+down[0],loc[1]+down[1])
            print("down loc : ",loc)
            if (loc[1] <= n and loc[1] >0):
                location = loc
                
            else:
                continue 
        elif i == "L": 
            loc += left
            if (loc[0] <= n and loc[0] >0):
                location = loc
            else:
                continue
        elif i == "R": 
            loc =  (loc[0]+right[0],loc[1]+right[1])
            print("loc:",loc)
            
            if (loc[0] <= n and loc[0] >0):
                location = loc
            else:
                continue

    return location

print(solution(["R","R","R","U","D","D"],5))

"""
이 문제는 요구사항대로 충실히 구현하면 되는 문제
일력의 명령에 따랄서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류된다. 
다만, 알고리즘 교재나 문제 출이 사이트에 따라 다르게 일컬을 수 있으므로, 코딩 테스트에서의 시뮬레이션 유형, 
구현 유형, 완전탐색유형은 서로 유사한 점이 많다는 점도만 기억하자.
"""

def solution2(arr,n):
    x,y = 1,1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    moveType = ['L','R','U','D']

    for plan in arr:
        for i in range(len(moveType)):
            if plan == moveType[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x,y = nx,ny

    return (x,y) 

print(solution2(["R","R","R","U","D","D"],5))