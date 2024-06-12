class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        tmp=3
        total = 0
        while tmp <= n:
            temp = tmp
            while temp:
                if temp%10 == 4:
                    print(f"tmp:{tmp}")
                    total += 1
                    break
                temp //= 10
            tmp += 1
        print(f"total:{total}")

temp = Solution()
print(temp.countNumberswith4(4))        