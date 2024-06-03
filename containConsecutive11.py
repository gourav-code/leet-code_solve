class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        #recursive solution F[n] = f[n-1] + f[n-2]
        # consecutive 11's is 2**n - f[n]
        arr = [2,3]
        if n == 1:
            return 2 - arr[0]
        if n == 2:
            return 4 - arr[1]
            
        m = 1000000007
        for i in range(3, n+1):
            tmp = arr[0] + arr[1]
            arr[0] = arr[1]
            arr[1] = tmp
            
        return (2**n - arr[1]) % m
# also works with python but python has integer size problem