from collections import deque

def main():
    n, m = map(int,input().split())
    cmp = [ [] for _ in range(n+1)]
    count= [0]*(n+1)
    q = deque()
    ans=[]
    for _ in range (m):
        a, b = map(int, input().split())
        cmp[a].append(b)
        count[b]+=1

    for i in range(1,n+1):
        if count[i]==0:
            q.append(i)

    while q:
        i = q.popleft()
        ans.append(i)
        for j in cmp[i]:
            count[j]-=1
            if count[j]==0:
                q.append(j)
    print(*ans)

if __name__=="__main__":
    main()
