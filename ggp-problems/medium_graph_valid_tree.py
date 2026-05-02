from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        map = defaultdict(list)
        for e1, e2 in edges:
            map[e1].append(e2)
            map[e2].append(e1)

        seen = set()

        def dfs(node):
            seen.add(node)
            for i in map[node]:
                if i not in seen:
                    dfs(i)

        dfs(0)

        return len(seen) == n
