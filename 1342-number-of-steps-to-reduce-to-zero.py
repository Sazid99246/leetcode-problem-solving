class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num -= 1
                steps += 1
        return steps

s = Solution()
print(s.numberOfSteps(14))