class Solution:
    def myAtoi(self, s: str) -> int:
#         flag = False
#         res = ""
#         for ch in s:
#             # check for whitespace
#             if ch == " ":
#                 continue
                
#             # check for sign
#             if ch == '-':
#                 flag = True
#                 continue
                
#             # check for words
#             if not str.isdigit(ch):
#                 continue
                
#             res += ch
#         num = int(res)
#         if flag:
#             num = -1 * num
            
#         min_int = 2 ** 31
        
#         if num > min_int - 1:
#             return min_int - 1
#         elif num < (-1 * min_int):
#             return -1 * min_int
            
#         return num

        s = s.lstrip()
        
        # If string is empty return 0
        if len(s) == 0:
            return 0

        # String index from where the processing should start
        start = 0
        
        # Handling numbers with +/- sign
        sign_multiplier = 1
        if s[0] == '-': # Handling for negative sign numbers
            sign_multiplier = -1
            start = 1
        elif s[0] == '+': # Handling for signed positive sign number
            start = 1

        result = 0

        index = start
        while index < len(s):
            # Handling for non numeric values
            if not('0' <= s[index] <= '9'):
                return result * sign_multiplier

            # Calculate the result for current iteration
            result = result * 10 + ord(s[index]) - ord('0')

            # Check if result exceeds MinInt32 or MaxInt32
            min_int_32 = 2 ** 31
            if result * sign_multiplier <= -min_int_32:
                return -min_int_32
            elif result * sign_multiplier >= min_int_32-1:
                return min_int_32-1
            index+=1

        return result * sign_multiplier