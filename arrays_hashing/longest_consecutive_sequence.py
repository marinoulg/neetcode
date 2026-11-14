class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_copy = nums.copy()
        print(nums_copy)
        consecutives = {}

        def find_consecutives(nums_copy, consecutives):
            maxi = max(nums_copy)
            if (maxi  - 1) in nums_copy:
                print("(maxi  - 1):", (maxi  - 1))
                if maxi not in consecutives:
                    consecutives[maxi] = []
                consecutives[maxi].append((maxi))
                consecutives[maxi].append((maxi-1))
                nums_copy.remove(maxi)
            else:
                nums_copy.remove(maxi)
            return nums_copy, consecutives, maxi

        # print(maxi)
        try:
            while True:
                nums_copy, consecutives, maxi = find_consecutives(nums_copy, consecutives)
                if maxi not in consecutives: consecutives[maxi] = [maxi]

        except:
            return list(consecutives.keys())


# nums=[0,3,2,5,4,6,1,1, 9, 10, 11]
nums = [2,20,4,10,3,4,5]

print(Solution().longestConsecutive(nums))
