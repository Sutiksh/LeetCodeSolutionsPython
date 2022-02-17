class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_positive = not ((dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0))
        
        if dividend == 0:
            return 0
        
        if abs(dividend) == abs(divisor):
            return 1 if is_positive else -1
        
        count = 0
        dividend, divisor = abs(dividend), abs(divisor)
        curr_sum = divisor
        
        while curr_sum <= dividend:
            i = 1
            while curr_sum + curr_sum < dividend:
                curr_sum = curr_sum + curr_sum
                i += i
            dividend -= curr_sum
            curr_sum = divisor
            count += i
        
        if dividend < 0:
            count -= 1
               
        if count > 2147483647:
            if is_positive:
                count = 2147483647
            elif count > 2147483648:
                count = 2147483648
        
        return count if is_positive else -count