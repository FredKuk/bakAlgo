def bfs(visit, graph, now) :
 if visit[now]==False:
  print(now)
  visit[now]=True
  
  stack +=graph[now]
  
  for next in stack:
   if visit[next]==False:
    print(next)
    visit[next]=True
    stack+=graph[next]
    
def dfs(visit,graph, now):
 if visit[now]==False:
  print(now)
  visit[now]=True
  for next in graph[now]:
   dfs(visit,graph,next)
   
def main() :
 n,m,v = map(int , input().split())
 visit = [False for _ in range(n+1)]
 graph = [[] for _ in range(n+1)]
 
 for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
 for i in range(m):
  graph[i].sort()
 
 dfs(visit,graph,v)
 
 visit=[False for _ in range(n+1)]
 
 print("------------------------------")
 
 bfs(visit,graph,v)
 
if __name__=="__main__" :
 main()
