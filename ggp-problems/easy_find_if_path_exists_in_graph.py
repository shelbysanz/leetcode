from collections import defaultdict, deque


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # base case
        if not edges and source == destination:
            return True

        # build graph
        graph = defaultdict(list)
        for i in edges:
            # since its undirected, its built both ways
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        # from source look for destination
        visited = defaultdict(int)
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if visited[node]:
                continue
            # check for destination node if found return true
            if destination in graph[node]:
                return True
            # if not there, queue the next vertices to look for a path
            queue.extend(graph[node])
            # process each one by one (keep track of processed nodes)
            visited[node] = 1

        # if we reach the end of processing, there is no path then return false
        return False
