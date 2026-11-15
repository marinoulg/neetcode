class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        def get_longest(mdict):
            longest = 0
            key = str()
            for k in mdict.keys():
                if len(set(mdict[k])) > longest:
                    longest = len(set(mdict[k]))
                    key = k
                elif key == str():
                    key = '*'
            return key

        nums = list(set(nums))
        nums = sorted(nums, reverse=True)

        if len(set(nums)) > 0 and len(set(nums)) != 1:
            mdict = {}
            maxi = nums[0]
            key = nums[0]

            for _ in range(1,len(nums)):
                if maxi - 1 == nums[1]:
                    if key not in mdict:
                        mdict[key] = [maxi-1]
                    else: mdict[key].append(maxi-1)
                    nums.pop(0)
                    maxi = nums[0]

                else:
                    nums.pop(0)
                    maxi = nums[0]
                    key = nums[0]

            k = get_longest(mdict)
            if k != "*" and k != '':
                res_tmp = (k, mdict[k])

                possibles = str(res_tmp).replace("(","").replace(")","").replace(":","").replace("[","").replace("]","").replace(",","")
                possibles = possibles.split()

                len(set(possibles))
                return len(set(possibles))
            else: return 1
        elif len(set(nums)) == 1: return 1
        else: return 0


nums=[2,20,4,10,18, 19, 3,4,5]
print(Solution().longestConsecutive(nums))
