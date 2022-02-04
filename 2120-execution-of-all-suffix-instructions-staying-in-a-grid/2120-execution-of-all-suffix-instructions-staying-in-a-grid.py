class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        x = startPos[0]
        y = startPos[1]
        result = []
        def factory(order,x,y):
            if order == "R":
                x,y = right(x,y)
            elif order == "L":
                x,y = left(x,y)
            elif order == "U":
                x,y = up(x,y)
            elif order == "D":
                x,y = down(x,y)
            else:
                print("something is wrong")
            return x,y
        #if x >= n or y >= n or x < 0 or y<0 -> stop
        def checker(x,y,n):
            if x >= n or y >= n or x<0 or y<0:
                return False
            else:
                return True
            
        def right(x,y):
            x += 1
            return x,y 
        def left(x,y):
            x -= 1
            return x,y
        def up(x,y):
            y -= 1
            return x,y
        def down(x,y):
            y += 1
            return x,y
        for i in range(0,len(s)):
            x = startPos[1]
            y = startPos[0]
            count = 0
            for order in s[i:]:
                x,y = factory(order,x,y)
                if checker(x,y,n):
                    count += 1
                else:
                    
                    break
            result.append(count)
        return result
