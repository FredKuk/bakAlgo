def main():
    s=input()
    sum=0
    for ch in s :
        if ch =='(' : sum+=1
        else : sum-=1
    print("YES") if sum==0 else print("NO")
    
if __name__=="__main__" :
    main()