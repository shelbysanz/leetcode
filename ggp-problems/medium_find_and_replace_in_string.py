from collections import defaultdict

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        hashmap = defaultdict(list)
        for i, tgt, src in zip(indices, targets, sources):
            hashmap[i].append((tgt, src))
        i, res = 0, []
        while i < len(s):
            replaced = False
            for r_tuple in hashmap[i]:
                tgt, src = r_tuple
                if s.startswith(src, i):
                    res.append(tgt)
                    i += len(src)
                    replaced = True
                    break
            if not replaced:
                res.append(s[i])
                i += 1

        return "".join(res)
