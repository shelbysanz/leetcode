class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        trust_scores = [0] * n
        for n1, n2 in trust:
            trust_scores[n1 - 1] -= 1
            trust_scores[n2 - 1] += 1

        for i in range(len(trust_scores)):
            if trust_scores[i] == (n - 1):
                return i + 1
        return -1
