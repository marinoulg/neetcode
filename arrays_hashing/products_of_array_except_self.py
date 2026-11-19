from math import prod
from pprint import pprint


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        def test(nums):
            print(len(nums))
            print(nums)
            new = {}
            for idx in range(len(nums)-1):
                new[idx] = (nums[idx]*nums[idx+1])

            new[len(nums)] = (nums[0]*nums[-1])
            idx = (list(new.values()))
            print(idx)

            if len(nums)%2==0:
                print("pair")
                """
                # one = [idx1 * nums[-1]] = 35*11=385
                # two = [idx2 * nums[0]] = 77*3=231
                # three = [idx3 * nums[1]] = 33*5=165
                # four = [idx0 * nums[2]] = 15*7=105

                # one = [idx1 * idx3 * nums[-1]] = 35*143*17=85085
                # two = [idx2 * id4 * nums[0]] = 77*221*3=51051
                # three = [idx3 * idx5 * nums[1]] = 143*51*5=36465
                # four = [idx4 * idx0 * nums[2]] = 221*15*7=23205
                # five = [idx5 * idx1 * nums[3]] = 51*35*11=19635
                # six = [idx0 * idx2 * nums[4]] = 15*77*13=15015

                # one = [idx1 * idx3 * idx5 * nums[-1]] = 35*143*323*23=37182145
                # two = [idx2 * id4 * idx6 * nums[0]] = 77*221*437*3=22309287
                # three = [idx3 * idx5 * idx7 * nums[1]] = 143*323*69*5=15935205
                # four = [idx4 * idx6 * idx0 * nums[2]] = 221*437*15*7=10140585
                # five = [idx5 * idx7 * idx1 * nums[3]] = 323*69*35*11=8580495
                # six = [idx6 * idx0 * idx2 * nums[4]] = 437*15*77*13=6561555
                # seven = [idx7 * idx1 * idx3 * nums[5]] = 69*35*143*17=5870865
                # eight = [idx0 * idx2 * idx4 * nums[6]] = 15*77*221*19=4849845
                """
                if len(nums) == 2:
                    res = [nums[1], nums[0]]

                elif len(nums) == 4:
                    one = idx[1] * nums[-1]
                    two = idx[2] * nums[0]
                    three = idx[3] * nums[1]
                    four = idx[0] * nums[2]
                    res = [one, two, three, four]

                elif len(nums) == 6:
                    one = idx[1] * idx[3] * nums[-1]
                    two = idx[2] * idx[4] * nums[0]
                    three = idx[3] * idx[5] * nums[1]
                    four = idx[4] * idx[0] * nums[2]
                    five = idx[5] * idx[1] * nums[3]
                    six = idx[0] * idx[2] * nums[4]
                    res = [one, two, three, four, five, six]

                elif len(nums) == 8:
                    one = idx[1] * idx[3] * idx[5] * nums[-1]
                    two = idx[2] * idx[4] * idx[6] * nums[0]
                    three = idx[3] * idx[5] * idx[7] * nums[1]
                    four = idx[4] * idx[6] * idx[0] * nums[2]
                    five = idx[5] * idx[7] * idx[1] * nums[3]
                    six = idx[6] * idx[0] * idx[2] * nums[4]
                    seven = idx[7] * idx[1] * idx[3] * nums[5]
                    eight = idx[0] * idx[2] * idx[4] * nums[6]
                    res = [one, two, three, four, five, six, seven, eight]

                elif len(nums) == 10:
                    one = idx[1] * idx[3] * idx[5] * idx[7] * nums[-1]
                    two = idx[2] * idx[4] * idx[6] * idx[8] * nums[0]
                    three = idx[3] * idx[5] * idx[7] * idx[9] * nums[1]
                    four = idx[4] * idx[6] * idx[8] * idx[0] * nums[2]
                    five = idx[5] * idx[7] * idx[9] * idx[1] * nums[3]
                    six = idx[6] * idx[8] * idx[0] * idx[2] * nums[4]
                    seven = idx[7] * idx[9] * idx[1] * idx[3] * nums[5]
                    eight = idx[8] * idx[0] * idx[2] * idx[4] * nums[6]
                    nine = idx[9] * idx[1] * idx[3] * idx[5] * nums[7]
                    ten = idx[0] * idx[2] * idx[4] * idx[6] * nums[8]
                    res = [one, two, three, four, five, six, seven, eight, nine, ten]

            else:
                print("impair")
                """
                # one = [idx1 * idx3] = 35*143=5005
                # two = [idx2 * id4] = 77*39=3003
                # three = [idx3 * idx0] = 143*15=2145
                # four = [idx4 * idx1] = 39*35=1365
                # five = [idx0 * idx2] = 15*77=1155

                # one = [idx1 * idx3 * idx5] = 35*143*323=1616615
                # two = [idx2 * id4 * idx6] = 77*221*57=969969
                # three = [idx3 * idx5 * nums[0]] = 143*323*15=692835
                # four = [idx4 * idx6 * nums[1]] = 221*57*35=440895
                # five = [idx5 * idx0 * idx2] = 323*15*77=373065
                # six = [idx6 * idx1 * idx3] = 57*35*143=285285
                # seven = [idx0 * idx2 * idx4] = 15*77*221=255255

                # one = [idx1 * idx3 * idx5 * idx7] = 35*143*323*667=1078282205
                # two = [idx2 * idx4 * idx6 * idx8] = 77*221*437*87=646969323
                # three = [idx3 * idx5 * idx7 * idx0] = 143*323*667*15=462120945
                # four = [idx4 * idx6 * idx8 * idx1] = 221*437*87*35=294076965
                # five = [idx5 * idx7 * idx0 * idx2] = 323*667*77*15=248834355
                # six = [idx6 * idx8 * idx1 * idx3] = 437*87*35*143=190285095
                # seven = [idx7 * idx0 * idx2 * idx4] = 667*15*77*221=170255085
                # eight = [idx8 * idx1 * idx3 * idx5] = 87*35*143*323=140645505
                # nine = [idx0 * idx2 * idx4 * idx6] = 15*77*221*437=111546435

                """
                if len(nums) == 1:
                    res = nums

                elif len(nums) == 3:
                    one = idx[1]
                    two = idx[2]
                    three = idx[0]
                    res = [one, two, three]

                elif len(nums) == 5:
                    one = idx[1] * idx[3]
                    two = idx[2] * idx[4]
                    three = idx[3] * idx[0]
                    four = idx[4] * idx[1]
                    five = idx[0] * idx[2]
                    res = [one, two, three, four, five]

                elif len(nums) == 7:
                    one = idx[1] * idx[3] * idx[5]
                    two = idx[2] * idx[4] * idx[6]
                    three = idx[3] * idx[5] * idx[0]
                    four = idx[4] * idx[6] * idx[1]
                    five = idx[5] * idx[0] * idx[2]
                    six = idx[6] * idx[1] * idx[3]
                    seven = idx[0] * idx[2] * idx[4]
                    res = [one, two, three, four, five, six, seven]

                elif len(nums) == 9:
                    one = idx[1] * idx[3] * idx[5] * idx[7]
                    two = idx[2] * idx[4] * idx[6] * idx[8]
                    three = idx[3] * idx[5] * idx[7] * idx[0]
                    four = idx[4] * idx[6] * idx[8] * idx[1]
                    five = idx[5] * idx[7] * idx[0] * idx[2]
                    six = idx[6] * idx[8] * idx[1] * idx[3]
                    seven = idx[7] * idx[0] * idx[2] * idx[4]
                    eight = idx[8] * idx[1] * idx[3] * idx[5]
                    nine = idx[0] * idx[2] * idx[4] * idx[6]
                    res = [one, two, three, four, five, six, seven, eight, nine]

            return (res)
        return test(nums)

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

nums=[2,2,0,2,2,0,0,2,2]
# nums=[2,4,-2,1,2,-1,4,1,3,-3,-1,2,1,2,1,-3,1,-1,1,3,3,-2,-2,3,-3,-1,1,-2,-4,-2]

# not_effective(nums)
print("solution")
print(Solution().productExceptSelf(nums))



"""
nums = [3,5,7,11]
len(nums) = 4
idxs = [15, 35, 77, 33]

[385, 231, 165, 105]
"""
# one = [idx1 * nums[-1]] = 35*11=385
# two = [idx2 * nums[0]] = 77*3=231
# three = [idx3 * nums[1]] = 33*5=165
# four = [idx0 * nums[2]] = 15*7=105

"""
nums = [3,5,7,11,13]
len(nums) = 5 ********IMPAIR********
idxs = [15, 35, 77, 143, 39]

[5005, 3003, 2145, 1365, 1155]
"""
# one = [idx1 * idx3] = 35*143=5005
# two = [idx2 * id4] = 77*39=3003
# three = [idx3 * idx0] = 143*15=2145
# four = [idx4 * idx1] = 39*35=1365
# five = [idx0 * idx2] = 15*77=1155

"""
nums = [3,5,7,11,13,17]
len(nums) = 6
idxs = [15, 35, 77, 143, 221, 51]

[85085, 51051, 36465, 23205, 19635, 15015]
"""
# one = [idx1 * idx3 * nums[-1]] = 35*143*17=85085
# two = [idx2 * id4 * nums[0]] = 77*221*3=51051
# three = [idx3 * idx5 * nums[1]] = 143*51*5=36465
# four = [idx4 * idx0 * nums[2]] = 221*15*7=23205
# five = [idx5 * idx1 * nums[3]] = 51*35*11=19635
# six = [idx0 * idx2 * nums[4]] = 15*77*13=15015

"""
nums = [3,5,7,11,13,17,19]
len(nums) = 7 ********IMPAIR********
idxs = [15, 35, 77, 143, 221, 323, 57]

[1616615, 969969, 692835, 440895, 373065, 285285, 255255]
"""
# one = [idx1 * idx3 * idx5] = 35*143*323=1616615
# two = [idx2 * id4 * idx6] = 77*221*57=969969
# three = [idx3 * idx5 * idx[0]] = 143*323*15=692835
# four = [idx4 * idx6 * idx[1]] = 221*57*35=440895
# five = [idx5 * idx0 * idx2] = 323*15*77=373065
# six = [idx6 * idx1 * idx3] = 57*35*143=285285
# seven = [idx0 * idx2 * idx4] = 15*77*221=255255

"""
nums = [3,5,7,11,13,17,19,23]
len(nums) = 8
idxs = [15, 35, 77, 143, 221, 323, 437, 69]

[37182145, 22309287, 15935205, 10140585, 8580495, 6561555, 5870865, 4849845]
"""
# one = [idx1 * idx3 * idx5 * nums[-1]] = 35*143*323*23=37182145
# two = [idx2 * id4 * idx6 * nums[0]] = 77*221*437*3=22309287
# three = [idx3 * idx5 * idx7 * nums[1]] = 143*323*69*5=15935205
# four = [idx4 * idx6 * idx0 * nums[2]] = 221*437*15*7=10140585
# five = [idx5 * idx7 * idx1 * nums[3]] = 323*69*35*11=8580495
# six = [idx6 * idx0 * idx2 * nums[4]] = 437*15*77*13=6561555
# seven = [idx7 * idx1 * idx3 * nums[5]] = 69*35*143*17=5870865
# eight = [idx0 * idx2 * idx4 * nums[6]] = 15*77*221*19=4849845

"""
nums = [3,5,7,11,13,17,19,23,29]
len(nums) = 9 ********IMPAIR********
idxs = [15, 35, 77, 143, 221, 323, 437, 667, 87]

[1078282205, 646969323, 462120945, 294076965, 248834355, 190285095, 170255085, 140645505, 111546435]
"""
# one = [idx1 * idx3 * idx5 * idx7] = 35*143*323*667=1078282205
# two = [idx2 * idx4 * idx6 * idx8] = 77*221*437*87=646969323
# three = [idx3 * idx5 * idx7 * idx0] = 143*323*667*15=462120945
# four = [idx4 * idx6 * idx8 * idx1] = 221*437*87*35=294076965
# five = [idx5 * idx7 * idx0 * idx2] = 323*667*77*15=248834355
# six = [idx6 * idx8 * idx1 * idx3] = 437*87*35*143=190285095
# seven = [idx7 * idx0 * idx2 * idx4] = 667*15*77*221=170255085
# eight = [idx8 * idx1 * idx3 * idx5] = 87*35*143*323=140645505
# nine = [idx0 * idx2 * idx4 * idx6] = 15*77*221*437=111546435

# nums[-2]*nums[0]\
                # * idx1 * idx3 * idx5= 23*3*35*143*323
