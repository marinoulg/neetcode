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
            if does_exist in numbers:
                possibles.append(tuple(sorted([elem, does_exist])))
            else:
                numbers.remove(elem)

        print(set(possibles))
        def length_is_1(possibles):
            left = list(set(possibles))[0][0]
            right = list(set(possibles))[0][1]
            # print(left, right)

            res = []
            print((keep_track_idx))
            if left != right: res.append((keep_track_idx[left][0], keep_track_idx[right][0]))
            else: res.append((keep_track_idx[left][0], keep_track_idx[right][1]))
            return list(res[0])

        if len(set(possibles)) == 1:
            res = length_is_1(possibles)
            return res
        else:
            for elem in possibles:
                a,b = elem
                if a == b:
                    possibles.remove(elem)
            # print(possibles)

        if len(set(possibles)) == 1:
            res = length_is_1(possibles)
            return res

        # return sorted([keep_track_idx[elem] for elem in possibles[0]])

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

numbers=[1,1,3,4]
target=2
print(Solution().twoSum(numbers = numbers, target = target))

# numbers=[10,20,30,45,50]
# target=60
# print(Solution().twoSum(numbers = numbers, target = target))
