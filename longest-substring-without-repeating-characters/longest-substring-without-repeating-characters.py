class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret, letter2lastIdx = 0, {}
        left = right = 0
        while right < len(s):
            if s[right] in letter2lastIdx:
                left = max(left, letter2lastIdx[s[right]]+1)
            ret = max(ret, right-left+1)            
            letter2lastIdx[s[right]] = right
            right += 1
        return ret         