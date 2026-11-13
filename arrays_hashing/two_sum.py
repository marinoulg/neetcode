class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_copy = nums.copy()

        def return_maxi(nums_copy):
            maxi_list = []
            for _ in range(1000):
                maxi = max(nums_copy)
                if (target - maxi) in nums_copy:
                    maxi_list.append(maxi)
                    break
                else:
                    nums_copy.remove(maxi)
            return maxi_list[0]

        maxi = return_maxi(nums_copy)

        def return_i(nums, target_bis, i_real=None):
            index_i = []
            for i in range(len(nums)):
                if nums[i] == target_bis and i != i_real:
                    index_i.append(i)
                    break
            return index_i[0]

        i = return_i(nums, target_bis=maxi)

        mini = target - maxi
        j = return_i(nums, target_bis=mini, i_real=i)

        return sorted([i,j])



# print(Solution().twoSum(nums = [0,4,3,0], target = 0))
# print(Solution().twoSum(nums = [2,6,5,4], target = 7))
print(Solution().twoSum(nums = [-3,4,3,90], target = 0))
