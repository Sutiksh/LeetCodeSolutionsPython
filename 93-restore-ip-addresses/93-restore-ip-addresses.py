class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #This will hold our results
        res = []
        
        #i will be the index of s we are currently evalulating
        #path will be the current IP address we are trying to construct. At most 4 Values inside of it        
        def backtracking(i, path):
            
            
            #If we're at an index that's greater than the length of our string, we've successfully moved through it
            #If we're at path length 4 as well, that means we have a valid IP address and can return append the value   
            if i == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            
            #This is if we've we've successfully iterated through the whole string but don't have a valid IP address
            #Because we don't have four number's in path            
            elif i == len(s) and len(path) != 4:
                return
            
            #Now we want starting adding to our path and do our backtracking
            #This adds the current character to the last value number in path            
            path[-1] += s[i]
            
            #We only want numbers at or below 255 to be added to our path
            if int(path[-1]) <= 255:
                
                 #We only want number's that don't start with zero to be added to our path, besides zero itself.
                if not(len(path[-1]) > 1 and path[-1][0] == '0'):
                    
                    #We recursively move on
                    backtracking(i + 1, path)
                    
            #We backtrack, removing the last character in the last value in path      
            path[-1] = path[-1][:-1]
            
            #We recursively move on
            backtracking(i + 1, path + [s[i]])
            return
        
        backtracking(1, [s[0]])
        
        return res