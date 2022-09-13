def main():
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int,input().split())))

    result=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            max1=0
            max2=0
            if i-1>=0:
                max1=result[i-1][j]
            if j-1>=0:
                max2=result[i][j-1]
            result[i][j]=arr[i][j]+max(max1,max2)
    print(result[n-1][m-1])

if __name__=="__main__":
    main()