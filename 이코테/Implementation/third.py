"""
문자열 재정렬 문제 
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 k1ka5cb7 이면 return = abckk13

"""
import re 
def solution(n:str):
    s = re.sub("[^a-zA-Z]","",n)
    sn = sorted(s)
    c = re.sub("[^0-9]","",n)
    c = [int(i) for i in c]
    result =""
    for i in sn:
        result +=i
    result += str(sum(c))

    return result

print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))

"""
요구사항대로 충실히 구현하면 되는 문제
문자열이 입력 되었을 떄 문자를 하나씩 확인합니다. 
숫자인 경우 따로 합계를 계산 
알파벳은 별도의 리스트에 저장 

알파벳 리스트는 정렬해 출력하고 합계를 붙여 출력하면 정답 
"""
# 이코테 
def solution2(n):
    result = [] 
    value = 0 

    for x in n:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()
    if value !=0:
        result.append(str(value))
    
    return "".join(result)


print(solution2("K1KA5CB7"))
print(solution2("AJKDLSI412K4JSJ9D"))