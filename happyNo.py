class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            tmp = 0
            while n > 0:
                temp = n % 10
                tmp = tmp + temp * temp
                n = n // 10
            return tmp
		visit = set()
        loop = True
        while loop:
            result = helper(n)
            if result == 1:
                return True
            elif n == result or result in visit:
                return False
			visit.add(result)
            print(f"result: {result}, n: {n}")
            n = result

last = Solution()
print(last.isHappy(n=19))
