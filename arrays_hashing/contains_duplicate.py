class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == len((set(nums))):
            return False
        else: return True

# nums = [1,2,3,4]
# print(len(nums))
# print(len(set(nums)))

# print(Solution().hasDuplicate(nums))
