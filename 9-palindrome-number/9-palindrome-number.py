class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        
        rev = 0
        
        while x > rev:
            dig = x % 10
            x = x // 10
            rev = rev * 10 + dig
            
        return True if (x == rev or x == rev // 10) else False