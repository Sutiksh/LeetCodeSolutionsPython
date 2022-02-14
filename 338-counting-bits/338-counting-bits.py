class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for num in range(n + 1):
            ans = 0
            i = num
            while i:
                i = i & (i - 1)
                ans += 1
            res.append(ans)
            
        return res
                