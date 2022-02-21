class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # * can symbolize empty string as well as any string
        # ? can symbolize any character
        # Dynamic programming : Using Matrix M with boolean values
        # Rows is for string s & columns is for pattern p
        # Adding extra row & column for initial conditions
        # The last value in matrix m is our result (m[rows-1][cols-1])
        
        rows, cols = (len(s)+1 , len(p)+1)
        
        # Initializing matrix with 'False'
        m = [[False for i in range(cols)] for j in range(rows)]
        
        #print ("Initialization: ",m)
        
        # Since empty string and empty pattern are a True match
        m[0][0] = True

        # Since empty pattern and any string are a False match
        # Initialize first column as 'False' : Already initialized

        # Since empty string and any pattern are not a straighforward 'T/F'
        # If we encounter a '*' we check the previous coulmn value and equate it to that.
        # If we encounter a character or '?', it is a 'False' match. : Already initialized 
        for j in range(1,cols):
            if (p[j-1] == '*'):
                m[0][j] = m[0][j-1] 
                
        #print ("Intial condtions: ",m)

        for i in range(1,rows): # Traversing through the string
            for j in range(1,cols): # Traversing through the pattern             
                # If we encounter same character in s and p, or '?' in p
                # Match is dependent on previous diagonal value 
                if ( s[i-1] == p[j-1] or p[j-1] == '?'):
                    m[i][j] = m[i-1][j-1]
                # If we encounter a '*' in p
                # Match is OR of upper row value (signifies previous state) and lower column value (signifies empty string)
                elif ( p[j-1] == '*'):
                    m[i][j] = m[i-1][j] or m[i][j-1]
                else:
                    # m[i][j] = False
                    continue

        #print ("Final State: ", m)
        return m[rows-1][cols-1]