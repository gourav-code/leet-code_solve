class Solution:
    def getCount(self, n):
        if n == 1:
            return 10
        
        l = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [1, 2, 3, 5],
            3: [2, 3, 6],
            4: [1, 4, 5, 7],
            5: [2, 4, 5, 6, 8],
            6: [3, 5, 6, 9],
            7: [4, 7, 8],
            8: [0, 5, 7, 8, 9],
            9: [6, 8, 9]
        }
        
        dp = [[0] * 10 for _ in range(n + 1)]
        
        for i in range(10):
            dp[1][i] = 1
        
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = sum(dp[length - 1][prev_digit] for prev_digit in l[digit])
        
        return sum(dp[n][i] for i in range(10))

# Example usage:
solution = Solution()
print(solution.getCount(1))  # Output: 10
print(solution.getCount(2))  # Output should match the actual count for sequences of length 2
#above is O(N) and O(N) time and space complexity respectively

# #User function Template for python3 My first solution
# class Solution:
# 	def getCount(self, n):
# 		# code here
# 		keypad = [
# 		    [1,2,3],
# 		    [4,5,6],
# 		    [7,8,9],
# 		    [-1,0,-1]
# 		    ]
# 	    RandC = [4, 3]
# 	    res = set()
# 	    def count(row, col, currStr):
# 	        nonlocal n
# 	        if n == len(currStr):
# 	            res.add(currStr)
# 	            return
	            
# 	        position = [[0,0],[1,0],[0,1],[-1,0],[0,-1]]
	        
# 	        for a,b in position:
# 	            r,c = row+a, col+b
# 	            if( r not in range(RandC[0]) or
# 	                c not in range(RandC[1]) or 
# 	                keypad[r][c] == -1 ):
# 	                    continue
#                 count(r,c,currStr+str(keypad[r][c]))
                
#         for i in range(RandC[0]):
#             for j in range(RandC[1]):
#                 if n>0:
#                     count(i,j,'')
                    
#         return len(res)