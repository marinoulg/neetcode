from math import prod

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def even_len_nums(nums, res, iteration, idx, adding_num):
            if iteration+adding_num < len(nums):
                res[iteration] *= idx[iteration+adding_num]
            else:
                res[iteration] *= idx[(iteration+adding_num) - len(nums)]
            # if iteration == 4:
            print(f"{adding_num} - {iteration}: {list(res.values())}")
            return res

        new = {}
        for idx in range(len(nums)-1):
            new[idx] = (nums[idx]*nums[idx+1])

        new[len(nums)] = (nums[0]*nums[-1])
        idx = (list(new.values()))
        print("nums:", nums)
        print("idx:", idx)
        print()

        res = {}
        def odd_len_nums(nums, res, iteration, idx, adding_num):
            if iteration+adding_num < len(nums):
                res[iteration] *= idx[iteration+adding_num]
            else:
                res[iteration] *= idx[(iteration+adding_num) - len(nums)]
            # if iteration == 4:
            print(f"{adding_num} - {iteration}: {list(res.values())}")
            return res

        if len(nums)%2==0:
            print("pair:", len(nums))

            res = {}
            for i in range(len(nums)):
                res[i] = 1

            adding_num = 1
            while adding_num < len(nums)-1:
                for iter in range(len(nums)): # iter = 4
                    res = even_len_nums(nums, res, iteration=iter, idx=idx, adding_num=adding_num)
                adding_num += 2
                # print(res)

            print("last step")
            for i in range(len(nums)):
                res[i] *= nums[i-1] # 4
            # print(f"{adding_num}: {list(res.values())}")

            return (list(res.values()))
        else:

                print("impair:", len(nums))

            # if len(nums) < 2:
            #     res = 1
            # else:
                res = {}
                for i in range(len(nums)):
                    res[i] = 1

                for i in range(len(nums)):
                    if i+1 < 3:
                        res[i] *= idx[i+1]
                    else:
                        res[i] *= idx[0]
                    print(list(res.values()))


            # elif len(nums) == 3:
            #     one = idx[1]
            #     two = idx[2]
            #     three = idx[0]
            #     res = [one, two, three]

            # elif len(nums) == 5:
            #     one = idx[1] * idx[3]
            #     two = idx[2] * idx[4]
            #     three = idx[3] * idx[0]
            #     four = idx[4] * idx[1]
            #     five = idx[0] * idx[2]
            #     res = [one, two, three, four, five]

            # elif len(nums) == 7:
            #     one = idx[1] * idx[3] * idx[5]
            #     two = idx[2] * idx[4] * idx[6]
            #     three = idx[3] * idx[5] * idx[0]
            #     four = idx[4] * idx[6] * idx[1]
            #     five = idx[5] * idx[0] * idx[2]
            #     six = idx[6] * idx[1] * idx[3]
            #     seven = idx[0] * idx[2] * idx[4]
            #     res = [one, two, three, four, five, six, seven]

            # elif len(nums) == 9:
            #     one = idx[1] * idx[3] * idx[5] * idx[7]
            #     two = idx[2] * idx[4] * idx[6] * idx[8]
            #     three = idx[3] * idx[5] * idx[7] * idx[0]
            #     four = idx[4] * idx[6] * idx[8] * idx[1]
            #     five = idx[5] * idx[7] * idx[0] * idx[2]
            #     six = idx[6] * idx[8] * idx[1] * idx[3]
            #     seven = idx[7] * idx[0] * idx[2] * idx[4]
            #     eight = idx[8] * idx[1] * idx[3] * idx[5]
            #     nine = idx[0] * idx[2] * idx[4] * idx[6]
            #     res = [one, two, three, four, five, six, seven, eight, nine]
        print()
        return (list(res.values()))


def not_effective(nums):
    print(len(nums))
    # (Solution().productExceptSelf(nums))
    print(nums)
    new = {}
    for idx in range(len(nums)-1):
        new[idx] = (nums[idx]*nums[idx+1])

    new[len(nums)] = (nums[0]*nums[-1])
    print(list(new.values()))

    print()

    neww = []
    for num in nums:
        copy = nums.copy()
        copy.remove(num)
        neww.append(prod(copy))

    print(neww)
    return neww

# nums=[2,2,0,1]
# nums = [1,2,4,6]
nums = [1,2,3]
# nums = [1,2,3,4,5,6,7,8,9,10]
# nums=[2,4,-2,1,2,-1,4,1,3,-3,-1,2,1,2,1,-3,1,-1,1,3,3,-2,-2,3,-3,-1,1,-2,-4,-2]
print(Solution().productExceptSelf(nums))
# not_effective(nums)
# print("solution")
# print(Solution().productExceptSelf(nums))

# nums = [1,2,4,6,5]
# for i in range(len(nums)):
#     prefix = nums[:i]
#     suffix = nums[i+1:]
#     print(prefix, suffix, end=": ")

#     if 0 in prefix or 0 in suffix:
#         print(0)
#     # elif 1 in prefix: prefix.remove(1)
#     # elif 1 in suffix: suffix.remove(1)
#     else: print()




    # tmp = 1
    # if prefix == []:
    #     for i in range(len(suffix)-2):
    #         elem = suffix[i]
    #         next_elem = suffix[i+1]
    #         tmp *= elem * next_elem
    #         i += 2
    #         print(tmp)
    # elif suffix == []:
    #     for i in range(len(prefix)-2):
    #         elem = prefix[i]
    #         next_elem = prefix[i+1]
    #         tmp = elem * next_elem
    #         i += 2
    #         print(tmp)
    # else:
    #     print()
    #     next


    # for pre in zip(prefis
    #     if len(prefix
