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
                """
                pair is only in all left
                """

                for i2 in range(len(left)-1):

                    # print("i1",i1, "—", "i2:", i2, end=": ")
                    num2 = left[i2]
                    num3 = left[i2+1]
                    # print("nums:", nums[i1], num2, num3)
                    if nums[i1] + num2 + num3 == 0 and i1 != i2 and i2!= i2+1 and i1 !=i2+1:
                        # print("nums:", nums[i1], num2, num3)
                        print(True, "left", nums[i1], nums[i2], nums[i2+1])
                        possibilities_idx.append((i1, i2+i1, i2+i1+1))
                        sorted_nums = tuple(sorted([nums[i1], num2, num3]))
                        poss_nums.append(sorted_nums)

                        if (nums[i1], nums[i2], nums[i2+1]) not in poss_dict:
                            # print("sorted_nums:",sorted_nums)
                            poss_dict[sorted_nums] = [(i1, i2, i2+1)]
                        else: poss_dict[sorted_nums].append((i1, i2, i2+1))

            if len(right) >= 2:
                """
                pair is only in all right
                """
                for i2 in range(len(right)-1):
                    if i2 != i1:
                        # print("i1",i1, "—", "i2:", i2)
                        num2 = right[i2]
                        num3 = right[i2+1]

                        if nums[i1] + num2 + num3 == 0 :
                            # print("nums:", nums[i1], num2, num3)
                            if i1 != i2 and i2!= i2+1 and i1 !=i2+1:
                                if i2 != 0:
                                    possibilities_idx.append((i1, i1, i2+i1+1))
                                    print(True, "right", nums[i1], nums[i1], nums[i2+i1+1])
                                    sorted_nums = tuple(sorted([nums[i1], num2, num3]))
                                    poss_nums.append(sorted_nums)

                                if (nums[i1], nums[i2], nums[i2+1]) not in poss_dict:
                                    # print("sorted_nums:",sorted_nums)
                                    poss_dict[sorted_nums] = [(i1, i2+i1, i2+1)]
                                # else: poss_dict[sorted_nums].append((i1, i2+i1, i2+i1+1))

            for i2 in range(len(left)):
                if i2 != i1:
                    for i3 in range(len(right)):
                        """
                        pair is combined in both left and right
                        ⚠️⚠️⚠️ pb is with indexes HERE

                        this should be sufficient bc above i am only checking consecutives
                        ⚠️ but need to pay more attention to the indexes here
                        """
                        if (left[i2]+nums[i1]+right[i3]) == 0 :
                                print((True, "both",nums[i1], left[i2], right[i3]), end=": ")
                                # print([i1], [i2], [i3], end=" // ")
                                # print([i1], [i2], [i1+i3])
                                # print(True, "both", nums[i1], nums[i2+i1], nums[i2+i1+1])

                                if i1 != i2 and i2!= i3 and i1 !=i1+i3:
                                    sorted_nums = tuple(sorted([nums[i1], left[i2], right[i3]]))
                                    poss_nums.append(sorted_nums)

                                    if (nums[i1], left[i2], right[i3]) not in poss_dict:
                                        poss_dict[sorted_nums] = [(i1, i1-i2, i1+i2+1)]
                                    # else: poss_dict[sorted_nums].append((i1, i1-i2, i2))



            print()

        pprint(poss_dict)
        print()

        # print(list(sorted(set(poss_nums))))
        return sorted(list(poss_dict.keys()))




# nums = [-1,0,1,2,-1,-4]
# nums=[0,1,1]

# nums=[3,0,-2,-1,1,2]
# nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
# nums=[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
# nums=[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
nums=[-1,-1,2,2,-4,0,1,3]


print(Solution().threeSum(nums))
# Output: [[-1,-1,2],[-1,0,1]]
