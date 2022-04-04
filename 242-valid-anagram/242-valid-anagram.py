from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        
        for ch in s:
            if countS != countT:
                return False
        
        return True