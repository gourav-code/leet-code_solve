class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        if len(a) == 0 or len(b) == 0:
            return -1
            
        sumA = sum(a)
        sumB = sum(b)
        
        if (sumA + sumB)%2 != 0:
            return -1

        a.sort()
        b.sort()
        
        i, j = 0, 0
        target = (sumB-sumA)//2
        while i< n and j < m:
            curr_diff = b[j] - a[i]
            if curr_diff == target:
                return 1
            elif curr_diff < target:
                j += 1
            else:
                i += 1
        
                    
        return -1

#below my solution and above chat gpt        
class Solution:
    def findSwapValues(self, a, b):
        # Your code goes here
        if len(a) == 0 or len(b) == 0:
            return -1
            
        sumA = sum(a)
        sumB = sum(b)
        
        if (sumA + sumB)%2 != 0:
            return -1

        a.sort()
        b.sort(reverse = True)
        
        prevA = -1
        observedVal = (sumB-sumA)//2
        for i in range(len(a)):
            if prevA == a[i]:
                continue
            prevA = a[i]
            needB = observedVal+a[i]
            for tmp in b:
                if tmp < needB:
                    break
                if tmp == needB:
                    return 1
                    
        return -1

temp = Solution()
print(temp.findSwapValues(a = [5, 7, 4, 6], b=[1, 2, 3,8]))