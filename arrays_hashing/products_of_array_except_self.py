from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def even_len_nums(nums, res, iteration, idx, adding_num):
            if iteration+adding_num < len(nums):
                res[iteration] *= idx[iteration+adding_num]
            else:
                res[iteration] *= idx[(iteration+adding_num) - len(nums)]
            # print(f"{adding_num} - {iteration}: {list(res.values())}")
            return res

        new = {}
        for idx in range(len(nums)-1):
            new[idx] = (nums[idx]*nums[idx+1])

        new[len(nums)] = (nums[0]*nums[-1])
        idx = (list(new.values()))
        # print("nums:", nums)
        # print("idx:", idx)
        # print()

        res = {}
        for i in range(len(nums)):
            res[i] = 1

        if len(nums)%2==0:
            # print("pair:", len(nums))
            adding_num = 1
            while adding_num < len(nums)-1:
                for iter in range(len(nums)): # iter = 4
                    res = even_len_nums(nums, res, iteration=iter, idx=idx, adding_num=adding_num)
                adding_num += 2

            # print("last step")
            for i in range(len(nums)):
                res[i] *= nums[i-1] # 4

            return (list(res.values()))
        else:
            # print("impair:", len(nums))

            adding_num = 1
            while adding_num < len(nums)-1:
                for iter in range(len(nums)):
                    res = even_len_nums(nums, res, iteration=iter, idx=idx, adding_num=adding_num)
                adding_num += 2
        return (list(res.values()))


# nums=[2,2,0,1]
# nums = [1,2,4,6]
# nums = [1,2,3,4,5]
# nums = [1,2,3,4,5,6,7,8,9,10]
nums=[2,4,-2,1,2,-1,4,1,3,-3,-1,2,1,2,1,-3,1,-1,1,3,3,-2,-2,3,-3,-1,1,-2,-4,-2]
print(Solution().productExceptSelf(nums))
