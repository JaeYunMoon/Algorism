"""
각 자리가 숫자0~9로만 이루어진 문자열 S가 주어졋을 떄, 왼쪽부터 오른쪽으로 하나씩 숫자를 확인하며 
숫자 사이에 'X'혹인 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
일반적인 사칙연산이 아닌 모든 연산은 왼쪽에서부터 순서대로 이뤄진다. 

예시)
02984 = ((((0+2)*9)*8)*4)
또한 만들어질 수 잇는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어진다. 
"""

def solution(arr):
    x = 0 
    for i in range(len(arr)):
        val = int(arr[i])
        if x == 1 or val == 1 or x == 0 or val == 0:
            x += val
        else:
            x *=val
        
    return x 

print(solution("02984"))

"""
- 대부분의 경우 '+' 보다는 'x'가 더 값을 크게 만듬 
- 다만 두 수 중에서 하나라도 0,1인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적
- 따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 
두 수가 모두 2이상인 경우에는 곱하면 정답 
"""
# 이코테 
def solution2(arr):
    result = int(arr[0])
    for i in range(1,len(arr)):
        num = int(arr[i])
        if num <=1 or result <=1:
            result += num
        else: 
            result *= num 
    return result 

print(solution2("02984"))

