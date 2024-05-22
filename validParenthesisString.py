class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0

        for tmp in s:
            if tmp == "(":
                leftMin += 1
                leftMax += 1
            elif tmp == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin <0:
                leftMin = 0

        return leftMin == 0
        