class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
                continue
            if not stack:
                return False

            last_pushed = stack.pop()
            match i:
                case ')':
                    if last_pushed != '(': return False
                case '}':
                    if last_pushed != '{': return False
                case ']':
                    if last_pushed != '[': return False

        return not stack
