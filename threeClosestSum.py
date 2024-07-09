from typing import List

class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        closest_sum = float('inf')
        
        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return current_sum  
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                elif abs(current_sum - target) == abs(closest_sum - target):
                    closest_sum = max(closest_sum, current_sum)
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
