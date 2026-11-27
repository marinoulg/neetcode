class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ""
        keep_track_idx = {}

        for idx in range(len(numbers)):
            if numbers[idx] not in keep_track_idx:
                keep_track_idx[numbers[idx]] = [idx+1]
            else: keep_track_idx[numbers[idx]].append(idx+1)

        i = -1
        elem = numbers[i]
        while elem >= target:
            numbers.pop(i)
            elem = numbers[i]
            # print(elem, i)

        print(keep_track_idx)

        possibles = []
        for i in range(len(keep_track_idx)-1):
            left = list(keep_track_idx.keys())[i]
            right = list(keep_track_idx.keys())[i+1]
            if left + right == target:
                possibles.append((keep_track_idx[left][0], keep_track_idx[right][0]))

        left, right = list(keep_track_idx.keys())[0], list(keep_track_idx.keys())[-1]
        if left + right == target:
                possibles.append((keep_track_idx[left][0], keep_track_idx[right][0]))

        return list(possibles[0])


# print(Solution().twoSum(numbers = [1,2,3,4], target = 3))

numbers=[2,3,4]
target=6

print(Solution().twoSum(numbers = numbers, target = target))
