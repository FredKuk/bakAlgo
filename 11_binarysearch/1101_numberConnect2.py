def getNum(n:int) :
    length=len(str(n))
    res=0
    for i in range(1,length):
        res+=i*(pow(10,i)-pow(10,i-1))
    res+= (n-pow(10,length-1)+1)*length
    return res

def main():
    n,k = map(int, input().split())
    if getNum(n)<k :
        print(-1)
        return
    
    left,right=1,n
    ans=0
    while left<=right:
        mid = (left+right)//2
        if getNum(mid)<k:
            left=mid+1
        else:
            right=mid-1
            ans=mid
    print(str(ans)[k-getNum(ans-1)-1])
if __name__ == "__main__":
    main()


# 문제
# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

# 1234567891011121314151617181920212223...

# 이렇게 만들어진 새로운 수에서, 앞에서 k번째 자리 숫자가 어떤 숫자인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000,000)과,  k(1 ≤ k ≤ 1,000,000,000)가 주어진다. N과 k 사이에는 공백이 하나 이상 있다.

# 출력
# 첫째 줄에 앞에서 k번째 자리 숫자를 출력한다. 수의 길이가 k보다 작아서 k번째 자리 숫자가 없는 경우는 -1을 출력한다.

# 예제 입력 1 
# 20 23
# 예제 출력 1 
# 6