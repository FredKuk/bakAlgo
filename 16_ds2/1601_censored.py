def main():
    A=list(input().rstrip())
    rA=list(reversed(A))
    T=input().rstrip()
    left=0
    right=len(T)-1
    front=[]
    back=[]
    flag=True
    while(left<=right):
        if flag:
            front.append(T[left])
            if len(front)>=len(A) and front[-len(A):] == A:
                front[-len(A):]=[]
                flag=False
            left+=1
        else:
            back.append(T[right])
            if len(back)>=len(A) and back[-len(A):]==rA:
                back[-len(A):]=[]
                flag=True
            right-=1
    while back:
        front.append(back.pop())
        if len(front)>=6  and front[-len(A):] == A:
            front[-len(A):]=[]
    print("".join(front))

if __name__=="__main__":
    main()