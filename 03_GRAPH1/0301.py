def dfs(rel,visit,depth,now) :
 if depth==5 :
  print("FIND!")
  exit()
 
 for next in rel[now]:
  if visit[now] == False :
   visit[now]=True
   dfs(rel,visit,depth+1,next)
   visit[now]=False

def main():
 n,m = map(int,input().split())
 
 rel=[[] for _ in range(n)]
 visit=[False for _ in range(n)]
 
 for _ in range(m) :
  a,b= map(int,input().split())
  rel[a].append(b)
  rel[b].append(a)
  
 for i in range(n) :
  dfs(rel,visit,1,i)
if __name__=="__main__" :
 main()