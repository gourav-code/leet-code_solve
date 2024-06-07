class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Create a list to keep track of the difference array
        arr = [0] * (maxx + 2)
        
        # Apply the range updates
        for i in range(n):
            arr[l[i]] += 1
            arr[r[i] + 1] -= 1
        
        # Find the maximum occurred integer using the prefix sum technique
        max_count, curr_count, result = 0, 0, -1
        for i in range(maxx + 1):
            curr_count += arr[i]
            if curr_count > max_count:
                max_count = curr_count
                result = i
        
        return result
## Below is my code
# class Solution:
#     #Complete this function
#     #Function to find the maximum occurred integer in all ranges.
#     def maxOccured(self,n, l, r, maxx):
#         ##Your code here
#         arr = [[0,0] for _ in range(maxx+1)]
#         #1 for start and -1 for end
#         for i in range(n):
#             arr[l[i]][0] += 1
#             arr[r[i]][1] += -1
            
#         result, curr_count, max_count = -1, 0, 0
#         for i in range(maxx+1):
#             curr_count += arr[i][0]
#             if curr_count > max_count:
#                 result = i
#                 max_count = curr_count
#             curr_count += arr[i][1]
                    
#         return result

# temp = Solution()
# print(temp.maxOccured(10, [4, 2, 3, 4, 4, 5, 2, 2, 4, 9], [8, 7, 9, 8, 7, 6, 4, 5, 9, 9], 9))
# print(temp.maxOccured(4, [1,4,3,1], [15,8,5,4], 15))
# print(temp.maxOccured(3, [2,1,3], [5,3,9], 9))
print(temp.maxOccured(5, [1,5,9,13,21], [15,8,12,20,30], 30))

