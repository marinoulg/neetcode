class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # k = le nombre de chiffres attendus dans l'array finale
        if len(nums) == k:
            return nums

        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        print(mydict)

        values = list(mydict.values())
        values_copy = values.copy()
        print("values:", values)

        keys = list(mydict.keys())
        keys_copy = keys.copy()
        print("keys:", keys)

        idx_keep = []
        def to_keep(values_copy):
            for i in range(len(values_copy)):
                if values_copy[i] == max(values_copy):
                    idx_keep.append(i)
                    values_copy.pop(i)
                    break
            return idx_keep, values_copy

        while len(idx_keep) < k:
            (idx_keep, values_copy) = to_keep(values_copy)

        # print("idx_keep:", idx_keep)
        # print("values_copy:", values_copy)
        result = []
        for idx in idx_keep:
            result.append(keys_copy[idx])

        return (result)







print(Solution().topKFrequent(nums = [1,4,4,3,3,3], k = 2))
print()
print(Solution().topKFrequent(nums = [1,2], k = 2))
