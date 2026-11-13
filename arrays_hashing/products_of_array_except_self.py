from math import prod
from pprint import pprint

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pprint(nums)
        new = {}
        for idx in range(len(nums)-1):
            new[idx] = (nums[idx]*nums[idx+1])

        new[len(nums)] = (nums[0]*nums[-1])
        print(list(new.values()))

        # for
        return new

nums = [1,2,4,6,5,12,10,34]
(Solution().productExceptSelf(nums))
print()

neww = []
for num in nums:
    copy = nums.copy()
    copy.remove(num)
    neww.append(prod(copy))

print(neww)

"""
nums = [1,2,4,6,5,12]
idxs = [2, 8, 24, 30, 60, 12]

[2880, 1440, 720, 480, 576, 240]
"""
# one = [idx1 * idx3 *idx5] = 8*30*12=2880
# two = [idx2 * idx4] = 24*60=1440
# three = [idx3 * idx5 * si dernier de la liste --> idx0] = 30*12*2=720
# four = [idx4 * idx1] = 2*8*30=480
# five = [idx5 * idx0 * idx2] = 12*2*24=576
# six = [idx1 * idx3] = 8*30=240


"""
nums = [1,2,4,6,5,12, 10]
idxs = [2, 8, 24, 30, 60, 12]

[28800, 14400, 7200, 4800, 5760, 2400, 2880]
"""
# one = [idx1 * idx3 *idx5] = 8*30*120=2880
# two = [idx2 * idx4] = 24*60=1440
# three = [idx3 * idx5 * idx0 * nums[-1]] = 30*12*2*10=7200
# four = [idx4 * idx6 * idx1] = 60*10*8=480
# five = [idx5 * idx0 * idx2] = 120*24*2=5760
# six = [idx6 * idx1 * idx3] = 10*8*30=2400
# seven = [idx0 * idx2 * idx4] = 24*60*2=2880

"""
nums = [1,2,4,6,5,12,10,34]
idxs = [2, 8, 24, 30, 60, 120, 340, 34]

[979200, 489600, 244800, 163200, 195840, 81600, 97920, 28800]
"""
# one = [idx1 * idx3 * idx5 * idx7] = 8*30*120*34=97920
# two = [idx2 * idx4 * idx6] = 24*60*340=489600
# three = [idx3 * idx5 * idx7 * idx0] = 30*120*34*2=244800
# four = [idx4 * idx6 * idx1] = 60*340*8=163200
# five = [idx5 * idx7 * idx2 * idx0] = 120*34*24*2=195840
# six = [idx6 * idx1 * idx3] = 340*8*30=81600
# seven = [idx7 * idx2 * idx4 * idx0] = 34*24*60*2=97920
# eight = [idx1 * idx3 * idx5] = 30*120*8=28800
