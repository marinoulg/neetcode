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

        # removed = []
        # for i in range(len(values)):
        #     # print(values[i])
        #     if values[i] < k:
        #         print(values[i])
        #         values_copy.remove(values[i])
        #         removed.append(i)

        # print(values_copy)
        # print(removed)

        keys = list(mydict.keys())
        keys_copy = keys.copy()
        print("keys:", keys)

        indexes_to_keep = []
        def indexes(indexes_to_keep, keys_copy):
            for i in range(len(keys_copy)):
                if max(keys_copy) == keys_copy[i]:
                    indexes_to_keep.append(i)
                    break
            keys_copy.remove(max(keys_copy))
            return indexes_to_keep, keys_copy

        indexes_to_keep, keys_copy = indexes(indexes_to_keep, keys_copy)
        indexes_to_keep, keys_copy = indexes(indexes_to_keep, keys_copy)
        indexes_to_keep, keys_copy = indexes(indexes_to_keep, keys_copy)

        # for idx in (indexes_to_keep):
        #     keys_copy
        print(indexes_to_keep)


        # try:
        #     for elem in removed:
        #         keys_copy.pop(elem)

        #     return (keys_copy)
        # except IndexError:
        #     return None






Solution().topKFrequent(nums = [1,4,4,3,3,3], k = 2)
# print(Solution().topKFrequent(nums = [1,2], k = 2))
