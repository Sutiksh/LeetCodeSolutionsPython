class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            p = str(sorted(i))
            # print("P:",p,end="")   # FOR YOUR BETTER UNDERSTANDING  I HAVE USED PRINT HERE 
            if p in d:
                d[p].append(i)
            else:
                d[p] = [i]
            # print("-->D:", d) # FOR YOUR BETTER UNDERSTANDING  I HAVE USED PRINT HERE
        final = []
        for j in d.values():
            final.append(j)
        return  (final)