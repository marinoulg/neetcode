from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        new = []
        for num in nums:
            copy = nums.copy()
            copy.remove(num)
            new.append(prod(copy))
        return new

print(Solution().productExceptSelf(nums = [1,2,4,6]))
