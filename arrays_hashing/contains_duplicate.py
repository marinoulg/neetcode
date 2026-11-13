class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            print("nums[i] =", nums[i])
            elem = nums[i]
            nums_copy = nums.copy()
            nums_copy.pop(i)
            for j in range(len(nums_copy)):
                print("nums[j] =",nums[j])
                if elem == nums_copy[j]:
                    return True
                else: next
        else:
            return False

print(Solution().hasDuplicate([1,2,3,4]))
