class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        lst = []
        for i in s:
            lst.append(d[i])
        ans = 0
        for i in range(len(lst)-1):
            if lst[i+1] > lst[i]:
                ans -= lst[i]
                continue
            ans += lst[i]
        return (ans+lst[-1])