class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # k = le nombre de chiffres attendus dans l'array finale
        if len(nums) == k:
            return (nums)

        mydict = {}
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        print(mydict)

        keys = list(mydict.keys())
        print("keys:", keys)

        values = list(mydict.values())
        print("values:", values)

        values_to_keep = (sorted(values, reverse=True)[:k])

        result = []
        for key, value in mydict.items():
            if value in values_to_keep:
                result.append(key)

        return sorted(result)

print(Solution().topKFrequent(nums = [1,4,4,3,3,3], k = 2))
print()
print(Solution().topKFrequent(nums = [1,2], k = 2))
print()
print(Solution().topKFrequent(nums=[1,1,1,2,2,3], k=2))
