import math
class Solution:
    def triangle_area(self,p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        
    def boundary_points(self,p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        tmp1 = math.gcd(abs(x2 - x1), abs(y2 - y1)) 
        tmp2 = math.gcd(abs(x3 - x2), abs(y3 - y2)) 
        tmp3 = math.gcd(abs(x1 - x3), abs(y1 - y3))
        print(f"tmp1,2,3: {tmp1},{tmp2},{tmp3}")
        return tmp1+tmp2+tmp3 
        
    def InternalCount(self, p, q, r):
        #code here
        area = self.triangle_area(p, q, r)
        print(f"area:{area}")
        boundary = self.boundary_points(p, q, r)
        print(f"boundary : {boundary}")
        return int(area - boundary / 2 + 1)

# class Solution:
#     def InternalCount(self, p, q, r):
#         #code here
#         x_start = min(p[0],q[0],r[0])
#         x_end = max(p[0],q[0],r[0])
#         y_start = min(p[1],q[1],r[1])
#         y_end = max(p[1],q[1],r[1])
        
#         diff_x = [q[0]-p[0],r[0]-q[0],p[0]-r[0]]
#         diff_y = [q[1]-p[1],r[1]-q[1],p[1]-r[1]]
        
#         count = 0
#         for i in range(x_start+1, x_end):
#             for j in range(y_start+1,y_end):
#                 a = diff_x[0]*(j-p[1])-diff_y[0]*(i-p[0])
#                 b = diff_x[1]*(j-q[1])-diff_y[1]*(i-q[0])
#                 c = diff_x[2]*(j-r[1])-diff_y[2]*(i-r[0])
#                 if a > 0 and b > 0 and c > 0:
#                     count += 1
#                 elif a < 0 and b < 0 and c < 0:
#                     count += 1

#         return count

temp = Solution()        
print(temp.InternalCount([0,0],[0,5],[5,0]))