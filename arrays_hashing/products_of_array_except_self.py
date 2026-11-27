from datetime import datetime

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def len_nums(nums, res, iteration, idx, adding_num):
            if iteration+adding_num < len(nums):
                res[iteration] *= idx[iteration+adding_num]
            else:
                res[iteration] *= idx[(iteration+adding_num) - len(nums)]
            return res

        def determine_sign_of_common_nums(nums, length_nums, res):
            middle = int(length_nums/2)
            left = nums[:middle]
            right = nums[middle:]

            c = 0
            for elem in left:
                if elem == -x: c += 1
            for elem in right:
                if elem == -x: c += 1
            if c%2==0: res[middle] = 1 * x
            else: res[middle] = -1 * x

            for i in range(len(left)):
                elem = left[i]
                if elem == -x: res[i] = res[middle] * -x
                else: res[i] = res[middle] * x

            for j in range(middle, middle+len(right)):
                elem = nums[j]
                if elem == -x: res[j] = res[middle] * -x
                else: res[j] = res[middle] * x
            return (list(res.values())), c, res[middle]

        new = {}
        length_nums = len(nums)
        for idx in range(length_nums-1):
            new[idx] = (nums[idx] * nums[idx+1])

        new[length_nums] = (nums[0] * nums[-1])
        idx = (list(new.values()))
        # print("nums:", nums)
        # print("idx:", idx)

        res = {}
        for i in range(length_nums):
            res[i] = 1

        set_nums = set(nums)
        list_nums_set = list(set(nums))

        x = list_nums_set[0] # using this condition to determine the sign of each new number
        if len(set_nums) == 2 and sorted(list_nums_set) == [-x,x] and length_nums > 2:
            if length_nums%2 != 0:
                res, c, res_middle = determine_sign_of_common_nums(nums, length_nums, res)
                return res

            elif length_nums%2 == 0:
                """
                problem is here
                """

                nums_bis = (nums[:-1])
                res, c, res_middle = determine_sign_of_common_nums(nums_bis, length_nums-1, res)
                for i in range(len(res)-1):
                    res[i] *= nums[-1]

                # print(res_middle)
                """
                more specifically, possibly here
                """
                if c%2==0: res[len(res)-1] = x * res_middle
                elif c%2!=0: res[len(res)-1] = -x * res_middle
                return res

        if length_nums%2==0:
            adding_num = 1
            while adding_num < length_nums-1:
                for iter in range(length_nums):
                    res = len_nums(nums, res, iteration=iter, idx=idx, adding_num=adding_num)
                adding_num += 2

            for i in range(length_nums):
                res[i] *= nums[i-1]

        else:
            adding_num = 1
            while adding_num < length_nums-1:
                for iter in range(length_nums):
                    res = len_nums(nums, res, iteration=iter, idx=idx, adding_num=adding_num)
                adding_num += 2
        return (list(res.values()))


# nums=[2,2,0,1]
# nums = [1,2,4,6]
# nums = [1,2,3,4,5]
# nums = [1,2,3,4,5,6,7,8,9,10]
# nums=[2,4,-2,1,2,-1,4,1,3,-3,-1,2,1,2,1,-3,1,-1,1,3,3,-2,-2,3,-3,-1,1,-2,-4,-2]
# nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,1,-1,1,1]
nums=[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
# nums=[1,-1,1,-1,1,-1]

print(len(nums))
# print((nums))
# print(nums[:3])
now = datetime.now()
res = Solution().productExceptSelf(nums)

# print(res)
after = datetime.now()
print(after - now)
