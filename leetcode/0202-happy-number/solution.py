class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        while True:
            if n == 1:
                return True
            if res < 10 and res % 2 == 0:
                break
            res = 0
            while n > 0:
                res = res + ((n % 10) * (n % 10))
                n //= 10
            n = res
        return False
