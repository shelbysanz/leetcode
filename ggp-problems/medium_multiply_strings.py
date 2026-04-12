class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # handle base case
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        # approach: box method, this is how i learned to multiply
        # create res array
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                ans_idx = i + j
                carry_idx = i + j + 1

                total = mul + res[carry_idx]

                res[ans_idx] += total // 10
                res[carry_idx] = total % 10
        return "".join(str(x) for x in res).lstrip("0")

assert Solution().multiply('123', '456') == '56088'