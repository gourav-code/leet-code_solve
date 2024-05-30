class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        left,right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []

        while(top < bottom and left < right):

            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            for j in range(top, bottom):
                result.append(matrix[j][right-1])
            right -= 1

            if not (top < bottom and left < right):
                return result

            for i in range(right-1, left-1,-1):
                result.append(matrix[bottom-1][i])

            bottom -= 1

            for j in range(bottom-1, top-1,-1):
                result.append(matrix[j][left])

            left +=1

        return result


tmp = Solution()
print(tmp.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))        