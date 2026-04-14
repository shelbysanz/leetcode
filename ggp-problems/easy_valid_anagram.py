from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # easiest solution
        # return Counter(s) == Counter(t)

        # this is essentially what counter does
        s_count = defaultdict(lambda: 0)
        t_count = defaultdict(lambda: 0)
        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        return s_count == t_count
