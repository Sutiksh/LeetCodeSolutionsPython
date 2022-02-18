class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words), len(words[0])
        w_count = Counter(words)
        res = []
        
        # unrelvent char may exist, which will let non-words appear
        # so start index should in len(word) range to deal with that senario
        for idx in range(n):
            ## each time we should build a count
            s_count = Counter()
            ## loop through s word by word
            for i in range(idx, len(s) - n + 1, n):
                word = s[i:i + n]
                ### check if its a valid word
                if word in w_count:
                    s_count[word] += 1
                
                if i >= n * m:
                    #### find the first word in s_count
                    first_word = s[(i - n * m): (i - n * m + n)]
                    if s_count[first_word] == 1:
                        del s_count[first_word]
                    else:
                        #### only if first word is valid should we do -1
                        #### otherwise s_count[some word] will less than 0
                        if first_word in w_count:
                            s_count[first_word] -= 1
                
                if w_count == s_count:
                    res.append(i - n * (m - 1))  
                    
        return res