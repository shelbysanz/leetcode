from collections import deque
class Solution:
    def __init__(self):
        self.store = deque([])

    def read(self, buf: List[str], n: int) -> int:
        count = 0
        while n > 0:
            if not self.store:
                ret = [""] * 4
                read4(ret)
                self.store.extend([i for i in ret if i != ""])
                if not self.store:
                    break
            buf[count] = self.store.popleft()
            n -= 1
            count += 1
        return count
