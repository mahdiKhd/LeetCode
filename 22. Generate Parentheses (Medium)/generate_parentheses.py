from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        remain_chars = 2*n
        stack = 0
        current = ''
        return self.gen(current, remain_chars, stack)

    def gen(self, current, remain_chars, stack):
        if stack < 0:
            return []
        if remain_chars < stack:
            return []
        if remain_chars == 0:
            return [current]

        if stack == 0:
            return self.gen(current + '(', remain_chars - 1, stack + 1)
        return self.gen(current + '(', remain_chars - 1, stack + 1) + self.gen(current + ')', remain_chars - 1, stack - 1)




solution = Solution()
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
print(solution.generateParenthesis(4))