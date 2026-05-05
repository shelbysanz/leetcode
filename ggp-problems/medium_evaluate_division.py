from collections import defaultdict, deque


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # build graph w/ edge weights
        adj = defaultdict(list)
        for e, w in zip(equations, values):
            u, v = e
            adj[u].append((v, w))
            adj[v].append((u, 1 / w))

        def bfs(root, target):
            queue = deque([(root, 1)])
            visited = set()
            while queue:
                u, curr = queue.popleft()
                if u == target:
                    return curr
                for v, w in adj[u]:
                    if v not in visited:
                        queue.append((v, curr * w))
                        visited.add(v)
            return -1

        output = []
        for u, v in queries:
            if u not in adj or v not in adj:
                output.append(-1)
                continue
            output.append(bfs(u, v))

        return output
