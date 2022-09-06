def bfs(visit,count, now, goal) :
    diff = abs(now-goal)
    
    l = []
    i=0
    
    l.append(now)
    visit[now]=True

    while(len(l)>i) :
        s=l[i]
        i+=1
        for next in [s+1,s-1,s*2]:
            if (next-goal)<diff and next>=0 and visit[next]==False:
                l.append(next)
                visit[next]=True
                count[next]=count[s]+1
    
def main() :
    n, k = map(int, input().split())
    max=200000
    visit = [False for _ in range(max+1)]
    count = [0 for _ in range(max+1)]

    bfs(visit,count,n,k)

    print(count[k])

if __name__=="__main__":
    main()

