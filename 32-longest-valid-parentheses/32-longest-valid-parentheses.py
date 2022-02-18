class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        
        stk = [-1]
        res = 0
        for i in range(len(s)):
            if (s[i] == '('):
                stk.append(i)
            else:
                stk.pop()
                if len(stk) == 0:
                    stk.append(i)
                else:
                    res = max(res, (i - stk[-1]))
        return res