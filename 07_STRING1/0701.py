def match(s, p) :
    print(s in p or p in s)
    ans = False
    for i in range(len(s)-len(p)):
        for j in range(len(p)):
            if s[i+j]==p[j] : 
                if(j==len(p)-1) : 
                    ans=True
                continue
            else : break
    print(ans)

def main() -> object:
    s = "ABCABDABCABEABC"
    p = "ABCABE"
    match(s,p)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("=============================================")
    print("Chapter ( 7 String ) // Number ( 1 ) // ^0^ ")
    print("=============================================")
    main()
    print("=============================================")