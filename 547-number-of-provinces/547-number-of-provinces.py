class Solution:
    def dfs(self, vertex: int, graph: List[List[int]], visited: set) -> [int]:
        traversalOrder = [vertex]
        visited.add(vertex)
        
        for city, isConnected in enumerate(graph[vertex]):
            if isConnected == 1 and city not in visited:
                traversalOrder += self.dfs(city, graph, visited)
        
        return traversalOrder
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## store all connected component and return the length of it
        visited = set()
        connectedComponents = []
        for city in range(len(isConnected)):
            if city not in visited:
                connectedComponents.append(self.dfs(city, isConnected, visited))
        ## You can print(connectedComponents) to see all the connectedComponents
        return len(connectedComponents)
        