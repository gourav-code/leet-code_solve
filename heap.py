#this solution is for permutation
class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []

        def allCombination(n,arr1):
            if n == 1:
                arr.append(arr1[:])
            else:
                allCombination(n-1, arr1)

                for i in range(n-1):
                    if n%2 == 0:
                        self.swap(arr1, i, n-1)
                    else:
                        self.swap(arr1, 0, n-1)

                    allCombination(n-1, arr1)

        allCombination(len(nums), nums)
        return arr


            
        