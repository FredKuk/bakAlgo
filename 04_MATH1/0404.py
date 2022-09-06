def gcd(a,b) :
 if b==0 : return a
 else : return gcd(b,a%b)
 
def main() :
 n = int(input("몇번하심 ? : "))
 ans = [[] for _ in range(n)]
 for k in range(n):
  l = list(map(int,input().split()))
  for i in range(len(l)):
   for j in range(i+1,len(l)):
    temp = gcd(l[i],l[j])
    ans[k].append(temp)
 for x in ans:
  print(x)
 
if __name__=="__main__":
 main()