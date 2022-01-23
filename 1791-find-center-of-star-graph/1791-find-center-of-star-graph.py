class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        new_edges = []
        for p1, p2 in edges:
            edge = set()
            edge.add(p1)
            edge.add(p2)
            new_edges.append(edge)
        print(new_edges)
            
        intersection = new_edges[0].intersection(*new_edges)
        return next(iter(intersection))