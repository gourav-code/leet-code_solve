class Solution:
    def smallestNumber(self, s, d):
        # code here
        arr = []
        if s > 9*d or s <= 0:
            return "-1"
        
        for _ in range(d):
            arr.append("0")
            
        num9 = s//9     #sum of digits is combination of s//9+s%9
        if num9>d:
            return "-1"
        i = -1
        while num9 > 0:
            i += 1
            arr[d-1-i] = "9"
            num9 -= 1
            
        if s%9 != 0:        
            i += 1
            arr[d-1-i] = str(s%9)
                   
        if arr[0] == "0":
            arr[0] = "1"                # making sure first number is not 0 like 023 if d == 3
            arr[d-1-i] = str(int(arr[d-1-i])-1)
            
        return "".join(arr)