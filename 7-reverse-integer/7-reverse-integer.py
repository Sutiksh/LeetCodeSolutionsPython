class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = x * sign
        max_int = 2 ** 31
        min_int = -1 * max_int
        while x:
            dig = x % 10
            x = x // 10
            res = res * 10 + dig
        
        if res > max_int or res < min_int:
            return 0
            
        return res * sign