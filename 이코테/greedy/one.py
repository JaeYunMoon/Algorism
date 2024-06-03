
"""
어떠한 수 N이 1이 될 때까지, 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다. 
단, 두번째 연산은 N이 k로 나누어 떨어질 때만 선택할 수 있습니다.

1. N에서 1을 뺍니다. 
2. N을 K로 나눕니다. 

N = 17, K = 4 일대 1번의 과정을 한번 수행 하면 16 이후 2번의 과정을 두번 수행하면 N은 1이 됩니다. 
실행한 횟수는 3이 됩니다. 과정을 수행하여야 하는 최소 횟수를 구하시오 

풀이 관련 아이디어 
- 주어진 N에 대하여 최대한 많이 나누기 # 그리디 
- N의 값을 줄 일 때 2이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 휠씬 빠르게 많이 줄일 수 있다. 
- 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?? # 그리디 풀기 전 항상 고민해야 할 것!
"""
def main(n,k):
    result = 0
    print(result)
    while not n==1 and not n < 0 :
        if not n % k ==0:
            s = n%k
            result += s # 그만큼 뺀다. 
            # print(result) # 뺀 수 
            n = (n - s)//k # 빼야 할 수 및 count 도 햇으니 빠로 빼고 나눠 줌 
            # print("n :",n)
            result +=1 
            # print(result)
        else:
            n = n // k 
            result +=1 
    return result

# 이코테 정답 
def main2(n,k):
    n,k = int(n),int(k)
    while True:
        target = (n//k) *k 
        result +=(n-target)
        n = target 
        if n<k:
            break
        result +=1 
        n //= k 

    resutl +=(n-1)
    return result 

# 시간 복잡도 : log 

if __name__ == "__main__":
    print("start")
    s = main(25,5)
    print(s)
