from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case
        if not s or not t:
            return ""

        t_counter = Counter(t)
        s_count = defaultdict(lambda: 0)

        have = 0
        need = len(t_counter)

        min_range = (0, 0)
        min_len = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1

            if c in t_counter and s_count[c] == t_counter[c]:
                have += 1
            while have == need:
                left_c = s[l]
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_range = (l, r+1)
                s_count[s[l]] -= 1
                if left_c in t_counter and s_count[left_c] < t_counter[left_c]:
                    have -= 1
                l += 1
        return s[min_range[0]:min_range[1]]
