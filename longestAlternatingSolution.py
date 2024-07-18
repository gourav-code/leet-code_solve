#O(n) solution, last solution might give intution for this solution

def alternatingMaxLength(self, arr):
    up = 1
    down = 1

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            up = down+1
        elif arr[i] < arr[i-1]:
            down = up + 1
    
    return max(up, down)

class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        lengthSubArray = [[1,'D']]*len(arr)
       
        for i in range(len(arr)-1,-1,-1):
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j]:
                    continue
                if j == len(arr)-1:
                    tmp = max(lengthSubArray[i][0],1+lengthSubArray[j][0])
                    if lengthSubArray[i][0]<1+lengthSubArray[j][0]:
                        tmp = 1+lengthSubArray[j][0]
                        if arr[i] > arr[j]:
                            lengthSubArray[i] = [tmp, 'D']
                        else:
                            lengthSubArray[i] = [tmp, 'U']
                if arr[i]>arr[j] and lengthSubArray[j][1] == 'U' and lengthSubArray[i][0] < 1+lengthSubArray[j][0]:
                    lengthSubArray[i] = [1+lengthSubArray[j][0], 'D']
                if arr[i]<arr[j] and lengthSubArray[j][1] == 'D' and lengthSubArray[i][0] < 1+lengthSubArray[j][0]:
                    lengthSubArray[i] = [1+lengthSubArray[j][0], 'U']
                    
        return lengthSubArray[0][0]



class Solution2:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        lengthSubArray = [[1, 'D']] * n
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if arr[i] > arr[j] and lengthSubArray[j][1] == 'U':
                    lengthSubArray[i] = max(lengthSubArray[i], [1 + lengthSubArray[j][0], 'D'], key=lambda x: x[0])
                if arr[i] < arr[j] and lengthSubArray[j][1] == 'D':
                    lengthSubArray[i] = max(lengthSubArray[i], [1 + lengthSubArray[j][0], 'U'], key=lambda x: x[0])
        
        return max(lengthSubArray, key=lambda x: x[0])[0]
# O(n^2) solution 
class Solution3:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        #code here
        if len(arr) == 0:
            return 0
            
        up = [1]*len(arr)
        down = [1]*len(arr)
        
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    up[i] = max(up[i], down[j]+1)
                elif arr[j] > arr[i]:
                    down[i] = max(up[j]+1, down[i])
                    
        return max(max(up), max(down))


temp = Solution()
arr = [20,19,9]
print(arr)
print(temp.alternatingMaxLength(arr))