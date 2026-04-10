class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        # initializing the next arrays
        next_even = [None] * n
        next_odd = [None] * n

        stack = []
        # sort by value in increasing order
        odd_pairs = sorted((val, idx) for idx, val in enumerate(arr))
        for val, idx in odd_pairs:
            while stack and idx > stack[-1]:
                prev = stack.pop()
                next_odd[prev] = idx
            stack.append(idx)

        stack = []
        # sort by decreasing order keep index
        even_pairs = sorted((-val, idx) for idx, val in enumerate(arr))
        for val, idx in even_pairs:
            while stack and idx > stack[-1]:
                prev = stack.pop()
                next_even[prev] = idx
            stack.append(idx)

        odd = [False] * n
        even = [False] * n

        odd[n - 1] = True
        even[n - 1] = True

        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                # checks if the even exists
                odd[i] = even[next_odd[i]]
            if next_even[i] is not None:
                # checks if the odd exists
                even[i] = odd[next_even[i]]

        # all valid indices start with odd jump
        return sum(odd)

