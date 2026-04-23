from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dist = ''
        curr = ''
        counts = defaultdict(int)
        n_counts = defaultdict(int)
        max_len = float('-inf')

        for i in s:
            if i == dist or i == curr:
                if i != curr:
                    dist, curr = curr, dist
                    n_counts[curr] = 0
            else:
                dist = curr
                curr = i
                counts[curr] = 0
                counts[dist] = n_counts[dist]
            n_counts[dist] = 0
            counts[curr] += 1
            n_counts[curr] += 1
            max_len = max(max_len, counts[dist] + counts[curr])

        return max_len
