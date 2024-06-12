class Solution:

    def nextGreaterElement(self, n: int) -> int:
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        digits = list(map(int, str(n)))  # Step 1: Convert the number to a list of its digits
        length = len(digits)
        
        # Step 2: Find the pivot
        pivot = -1
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break
        
        if pivot == -1:
            return -1  # The digits are in descending order; no greater number is possible
        
        # Step 3: Find the smallest digit larger than the pivot
        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                # Step 4: Swap
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break
        
        # Step 5: Sort the digits to the right of the pivot
        digits = digits[:pivot + 1] + sorted(digits[pivot + 1:])
        
        # Convert list of digits back to an integer
        result = int(''.join(map(str, digits)))
    

        if INT_MIN <= result <= INT_MAX:
            return result
        else:
            return -1