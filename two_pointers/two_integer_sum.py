class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ""
        keep_track_idx = {}
        for idx in range(len(numbers)):
            if numbers[idx] not in keep_track_idx:
                keep_track_idx[numbers[idx]] = [idx+1]
            else: keep_track_idx[numbers[idx]].append(idx+1)

        possibles = []
        for elem in numbers[::-1]:
            does_exist = target - elem
            # print(elem, does_exist)
            if does_exist in numbers:
                possibles.append(tuple(sorted([elem, does_exist])))
            else:
                numbers.remove(elem)
        # print(numbers)

        # print(set(possibles))
        if numbers != []:
            possibles = numbers # bc always 1 possible solution
            return sorted([keep_track_idx[elem][0] for elem in possibles])
        else: return []


print(Solution().twoSum(numbers = [1,2,3,4], target = 3))

# numbers=[2,3,4]
# target=6
# print(Solution().twoSum(numbers = numbers, target = target))

# numbers=[-1,0]
# target=-1
# print(Solution().twoSum(numbers = numbers, target = target))

# numbers=[-5,-3,0,2,4,6,8]
# target=5
# print(Solution().twoSum(numbers = numbers, target = target))

# numbers=[-10,-5,0,3,7]
# target=-2
# print(Solution().twoSum(numbers = numbers, target = target))
