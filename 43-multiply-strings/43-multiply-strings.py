class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans1=0
        ans2=0 
        for d in num1: ans1=ans1*10+(ord(d)-ord('0'))
        for d in num2: ans2=ans2*10+(ord(d)-ord('0'))
        return str(ans1*ans2)