def main() -> object:
    s = input()
    ans=[s[0]]
    find=False
    for i in range(1,len(s)):
        if find==True:
            ans.append(s[i])
            find=False
        if s[i]=='-':
            find=True
    print(''.join(ans))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("=============================================")
    print("Chapter ( 7 String ) // Number ( 2 ) // ^0^ ")
    print("=============================================")
    main()
    print("=============================================")#