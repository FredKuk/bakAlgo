from collections import deque
def go(now):
    result=[]
    result.append(now*2%10000)
    result.append(9999 if now==0 else now-1)
    result.append((now%1000)*10+now//1000)
    result.append((now%10)*1000+now//10)
    print(result)
    return result

def bfs(input,goal):
    next=["D","S","L","R"]
    visited=set()
    q=deque()
    q.append((input,""))
    flag=False
    while(q):
        if flag: break
        now,re= q.popleft()
        temp=go(now)
        for i in range(len(temp)):
            if temp[i] in visited: continue
            if temp[i]==goal:
                print(re+next[i])
                flag=True
                break
            else :
                visited.add(temp[i])
                q.append((temp[i],re+next[i]))
    

def main():
    n=input()
    for i in range(int(n)):
        x,y = map(int, input().split(" "))
        bfs(x,y)

if __name__=="__main__":
    main()
