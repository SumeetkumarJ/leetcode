
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # If opening bracket, push into stack
            if char in "({[":
                stack.append(char)

            # If closing bracket
            else:

                # Check if stack is empty or brackets don't match
                if not stack or stack[-1] != mapping[char]:
                    return False

                # Remove matching opening bracket
                stack.pop()

        # Valid only if stack is empty
        return len(stack) == 0
