import sys
def main():
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    arr = list(map(int, input().rstrip().split()))
    arr_sum=[0]*(N+1)
    arr_sum[0]=arr[0]
    for i in range(1,N):
        arr_sum[i]=arr_sum[i-1]+arr[i]
    for i in range(M):
        start,end=map(int, input().rstrip().split())
        if start>1:
            print(arr_sum[end-1]-arr_sum[start-2])
        else :
            print(arr_sum[end-1])

if __name__=='__main__':
    main()