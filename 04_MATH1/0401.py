def main():
 A,B,C=map(int,input().split())
 print((A+B)%C)
 print(((A%C)+(B%C))%C)
 print((A*B)%C)
 print(((A%C)*(B%C))%C)

if __name__=="__main__" :
 main()