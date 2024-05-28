#above  solution is of chat gpt
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        
        return result

#below solution is mine 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00
        if n == 1:
            return x
        if x == 0.00 or x == 1.00:
            return x

        tmp_pow = abs(n)
        tmp = 1.0000
        if tmp_pow%2==0:
            tmp = self.myPow(x,tmp_pow//2)
            tmp = tmp**2
        else:
            tmp = self.myPow(x,(tmp_pow-1)//2)
            tmp = (tmp**2)*x

        if n>0:
            return tmp
        else:
            return 1/tmp