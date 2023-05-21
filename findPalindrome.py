
def subPart(l: int, r: int, s: str, res: str) -> str:
    resLen = len(res)
    while(l>=0 and r<len(s) and s[l]==s[r]):
            if(r-l+1) > resLen:
                res = s[l:r+1]
                resLen = len(res)
            r+=1
            l-=1
    # print(f"11 {res}")
    return res

def main():
    s = input("Enter a string:" )
    res = ""
    resLen = 0
    for i,temp in enumerate(s):
        #for odd length
        if(len(s) % 2 != 0):
            l,r = i,i

            res = subPart(l, r, s, res)
        else:
            l,r = i,i+1

            res = subPart(l, r, s, res)

    print(res)



if __name__ == "__main__":
    main()

