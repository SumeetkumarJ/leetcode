
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i = 0  # Pointer for string
        j = 0  # Pointer for pattern

        star = -1
        match = 0

        while i < len(s):

            # Characters match or pattern has '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Pattern has '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Previous '*' matches one more character
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # No match possible
            else:
                return False

        # Ignore remaining '*' characters
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
