def start():
 n = int(input())
 nums=[]
 for _ in range(n) :
  temp=int(input())
  nums.append(temp)
 mx= 4 if max(nums)<3 else max(nums)+1
 arr=[0 for _ in range(mx)]
 arr[1]=1
 arr[2]=2
 arr[3]=4
 
 for i in range(4,len(arr)):
  arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
  
 for num in nums:
  print(arr[num])
 
if __name__=="__main__" :
 start()