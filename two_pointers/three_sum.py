from pprint import pprint
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        possibilities_idx = []
        poss_nums = []
        poss_dict = {}
        for i1 in range(len(nums)):
            left = nums[:i1+1]
            right = nums[i1:]

            print(i1, end = ": ")
            print(left, right)

            if len(left) >=2:
                for i2 in range(len(left)-1):
                    print("i1",i1, "—", "i2:", i2, end=": ")
                    num2 = left[i2]
                    num3 = left[i2+1]
                    print("nums:", nums[i1], num2, num3)
                    if nums[i1] + num2 + num3 == 0 and i1 != i2 and i2!= i2+1 and i1 !=i2+1:
                        print(True, "left", nums[i1], nums[i2], nums[i2+1])
                        possibilities_idx.append((i1, i2+i1+i1, i2+i1+1))
                        poss_nums.append((nums[i1], nums[i2], nums[i2+1]))

                        if (nums[i1], nums[i2], nums[i2+1]) not in poss_dict:
                            sorted_nums = tuple(sorted([nums[i1], nums[i2], nums[i2+1]]))
                            # print("sorted_nums:",sorted_nums)
                            poss_dict[sorted_nums] = [(i1, i2, i2+1)]
                        else: poss_dict[sorted_nums].append((i1, i2, i2+1))

            if len(right) >= 2:
                for i2 in range(len(right)-1):
                    print("i1",i1, "—", "i2:", i2)
                    num2 = right[i2]
                    num3 = right[i2+1]
                    print("nums:", nums[i1], num2, num3)
                    if nums[i1] + num2 + num3 == 0 :
                        if i1 != i2 and i2!= i2+1 and i1 !=i2+1:
                            possibilities_idx.append((i1, i2+i1, i2+i1+1))
                            print(True, "right", nums[i1], nums[i2+i1], nums[i2+i1+1])
                            poss_nums.append((nums[i1], nums[i2+i1], nums[i2+i1+1]))

                            if (nums[i1], nums[i2], nums[i2+1]) not in poss_dict:
                                sorted_nums = tuple(sorted([nums[i1], nums[i2+i1], nums[i2+i1+1]]))
                                # print("sorted_nums:",sorted_nums)
                                poss_dict[sorted_nums] = [(i1, i2+i1, i2+i1+1)]
                            else: poss_dict[sorted_nums].append((i1, i2+i1, i2+i1+1))
            print()

        pprint(poss_dict)

        print()
        return list(poss_dict.keys())



# nums = [-1,0,1,2,-1,-4]
# nums=[3,0,-2,-1,1,2]
nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]


print(Solution().threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]
