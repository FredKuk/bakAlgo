def gcd(a,b) :
 if b==0: return a
 else : return gcd(b,a%b)
 
def main():
 n=int(input())
 for _ in range(n) :
  a,b=map(int, input().split())
  ans=gcd(a,b)
  print(ans*a//ans*b//ans)
  
if __name__=="__main__":
 main()