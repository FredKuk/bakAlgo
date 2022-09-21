import sys
from collections import deque
def main():
    input=sys.stdin.readline
    n=int(input().rstrip())
    m=int(input().rstrip())

    edge=[[] for _ in range(n+1)]
    edge_R=[[] for _ in range(n+1)]
    cnt=[0]*(n+1)
    costs=[0]*(n+1)

    for _ in range(m):
        departure,arrival,cost=map(int,input().rstrip().split())
        edge[departure].append((arrival,cost))
        edge_R[arrival].append((departure,cost))
        cnt[arrival]+=1

    start,finish= map(int, input().rstrip().split())

    q=deque()
    q.append(start)

    while q :
        now = q.popleft()
        for to, cost in edge[now]:
            costs[to]=max(costs[to],costs[now]+cost)
            cnt[to]-=1
            if not cnt[to] :
                q.append(to)

    print(costs[finish])

    visit=[False]*(n+1)
    visit[finish]=True
    cnt=[0]*(n+1)

    q=deque()
    q.append(finish)

    ans=0
    while q:
        now=q.popleft()
        for to, cost in edge_R[now]:
            if costs[now]==costs[to]+cost:
                ans+=1
                if not visit[to] :
                    visit[to]=True
                    q.append(to)
    print(ans)

if __name__=="__main__":
    main()
