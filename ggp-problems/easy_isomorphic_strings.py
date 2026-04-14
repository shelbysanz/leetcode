class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_val = s[i]
            t_val = t[i]

            s_mapped = s_map.get(s_val)
            t_mapped = t_map.get(t_val)

            if not s_mapped and not t_mapped:
                s_map[s_val] = t_val
                t_map[t_val] = s_val
                continue

            if s_mapped != t_val or t_mapped != s_val:
                return False

        return True
