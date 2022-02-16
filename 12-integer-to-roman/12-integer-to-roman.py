class Solution:
    def intToRoman(self, num: int) -> str:
        d = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,  'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4,'I':1}
        s = ""
        for i, j in d.items(): # Bring from 'M':1000 to 'I':1 one by one
            while True:
                if num >= j: # If n is greater than or equal to j then
                    num -= j # Subtract the value from n
                    s += i # Add the chracter to s
                    continue # Repeat!
                else: # If not
                    break
        return s