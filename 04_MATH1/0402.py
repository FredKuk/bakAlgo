def cal_gcd (a,b):
 if b==0 :
  return a
 return cal_gcd(b,b%a)
 
def main():
 a, b = map(int,input().split())
 gcd = cal_gcd(a,b)
 
 print(gcd)
 print(gcd * a//gcd * b//gcd)
 
if __name__=="__main__" :
 main()