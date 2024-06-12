#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here 
        a0 = 1
        a1 = 1
        a2 = 1
        Sol = 0
        mod = 10**9+7
        if n<3:
            return 1
        
        for i in range(3,n+1):
            Sol = (a1 + a0)%mod
            a0 = a1
            a1 = a2
            a2 = Sol
            
        return Sol