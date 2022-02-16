class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        idx = 0
        if len(s) == 0:
            return 0
        
        if s[0] == '-':
            sign = -1
            idx = 1
        elif s[0] == '+':
            idx = 1
            
        res = 0
        for i in range(idx, len(s)):               
            # check for words
            if not str.isdigit(s[i]):
                return res * sign
                
            res = res * 10 + ord(s[i]) - ord('0')
            min_int = 2 ** 31
        
            if res * sign >= min_int - 1:
                return min_int - 1
            elif res * sign <= (-1 * min_int):
                return -1 * min_int

        
        return res * sign

#         while index < len(s):
#             # Handling for non numeric values
#             if not('0' <= s[index] <= '9'):
#                 return result * sign_multiplier

#             # Calculate the result for current iteration
#             result = result * 10 + ord(s[index]) - ord('0')

#             # Check if result exceeds MinInt32 or MaxInt32
#             min_int_32 = 2 ** 31
#             if result * sign_multiplier <= -min_int_32:
#                 return -min_int_32
#             elif result * sign_multiplier >= min_int_32-1:
#                 return min_int_32-1
#             index+=1

#         return result * sign_multiplier