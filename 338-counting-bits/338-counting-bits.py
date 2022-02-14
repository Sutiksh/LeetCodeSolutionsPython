class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n + 1):
            bn = bin(i).replace("0b", "")
            res.append(self.countOnes(bn))
        
        return res
        
    
    def countOnes(self, s):
        count = 0
        for b in s:
            if b == '1':
                count += 1
            
        return count
                