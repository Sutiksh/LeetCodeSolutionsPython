class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        if (len(haystack)==0) and (len(needle) == 0):
            return 0
        else: 
            if len(needle)>len(haystack): 
                return -1

            else: 
                for i in range(len(haystack)): 
                    if haystack[i:len(needle)+i] == needle:
                        return i
            return -1
        