def main() :
 s = input()
 pre=False
 line = 0
 sum=0
 for ch in s :
  if ch=='(' :
   pre=True
   line+=1
  if ch==')':
   line-=1
   if pre==True :
    sum+=line
   else :
    sum+=1
   pre=False
 print(sum)
 
if __name__=="__main__":
 main()