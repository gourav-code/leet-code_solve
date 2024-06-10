# User function Template for python3
class Solution:
    def merge_sort_in_place(self, arr, left, right, arr2):
        if right - left > 1:
            mid = (left + right) // 2
            self.merge_sort_in_place(arr, left, mid, arr2)
            self.merge_sort_in_place(arr, mid, right, arr2)
            self.merge(arr, left, mid, right, arr2)

    def merge(self, arr, left, mid, right, arr2):
        left_start = left
        right_start = mid
    
        while left_start < mid and right_start < right:
            if ord(arr[left_start]) <= ord(arr2[right_start]):
                left_start += 1
            else:
                value = arr[right_start]
                index = right_start
    
                while index > left_start:
                    arr[index] = arr[index - 1]
                    arr2[index] = arr2[index - 1]
                    index -= 1
    
                arr[left_start] = value
                arr2[left_start] = value
    
                left_start += 1
                mid += 1
                right_start += 1

    def matchPairs(self, n, nuts, bolts):
        for i in range(n):
            bolts[i] = nuts[i]
        self.merge_sort_in_place(nuts, 0, n, bolts)
        print(f"nuts: {nuts}")
        print(f"bolts: {bolts}")

temp = Solution()
temp.matchPairs(5, ['@', '%', '$', '#', '^'], ['%', '@', '#', '$', '^'])