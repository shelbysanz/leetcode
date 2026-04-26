class Solution:
    def getParts(self, str_val):
        str_val += "*"
        parts = []
        c_count, c_val = 1, str_val[0]
        for i in range(1, len(str_val)):
            if c_val != str_val[i]:
                parts.append((c_val, c_count))
                c_count = 1
                c_val = str_val[i]
            else:
                c_count += 1
        return parts

    def expressiveWords(self, s: str, words: list[str]) -> int:
        if not s or not words:
            return 0

        parts = self.getParts(s)
        matches = 0
        for word in words:
            word = self.getParts(word)
            if len(word) != len(parts):
                continue
            isMatch = True
            for i in range(len(word)):
                w_char, p_char = word[i][0], parts[i][0]
                w_count, p_count = word[i][1], parts[i][1]

                if w_char != p_char:
                    isMatch = False
                    break
                if p_count < w_count or (p_count < 3 and p_count != w_count):
                    isMatch = False
                    break
            matches += 1 if isMatch else 0
        return matches
