## Number of rectangle that can be fit inside a circle of r radius
#A rectangle with length l and width w can be inscribed in a circle if its diagonal is less than or equal to the diameter of the circle. 
#hence the condition

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        condition = 4*r*r
        for i in range(1,2*r):
            for j in range(1,2*r):
                if i*i + j*j <= condition:
                    count += 1
        return count