class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0

        for character in s:
            if character == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif character == ')':
                current_depth -= 1

        return max_depth

        