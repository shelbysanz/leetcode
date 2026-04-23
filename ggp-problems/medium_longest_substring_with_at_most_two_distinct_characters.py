from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r, max_len = 0,0,0
        map = defaultdict(int)

        def handleOldestIndex():
            """
            removes smallest index from map
            returns the index l should be at
            """
            smallest = float('inf')
            smallest_i = None
            for i in map:
                if map[i] < smallest:
                    smallest = map[i]
                    smallest_i = i
            del map[smallest_i]
            return smallest + 1

        while r < len(s):
            map[s[r]] = r
            if len(map) == 3:
                l = handleOldestIndex()
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
