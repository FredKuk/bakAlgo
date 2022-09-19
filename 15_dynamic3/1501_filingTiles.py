def main():
    n = int(input().strip())
    if n%2!=0 : return 0

    arr = [0]*(n//2+1)
    arr[0]=1
    arr[1]=3
    for i in range(2, n//2+1):
        arr[i]+=arr[i-1]*arr[1]
        for j in range(2,n//2+1):
            arr[i]+=2*arr[i-j]
    return arr[n//2]

if __name__=="__main__":
    print(main())

# '''
# 문제
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
#
# 출력
# 첫째 줄에 경우의 수를 출력한다.
#
# 예제 입력
# 2
# 예제 출력
# 3
# '''