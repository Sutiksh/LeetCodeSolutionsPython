class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True;
        EDGES = {  };
        for u, v in edges:
            if u not in EDGES:
                EDGES[u] = [v];
            else:
                EDGES[u].append(v);
            if v not in EDGES:
                EDGES[v] = [u];
            else:
                EDGES[v].append(u);
        
        q = deque([source]);
        visited = set();
        visited.add(source);
        while q:
            current = q.popleft();
            for nbr in EDGES[current]:
                if nbr not in visited:
                    visited.add(nbr);
                    if nbr == destination:
                        return True;
                    q.append(nbr);
        return False;
            