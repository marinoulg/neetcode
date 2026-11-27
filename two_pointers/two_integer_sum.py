class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ""
        indexes = []
        for i in range(len(numbers))[::-1]:
            elem = numbers[i]
            # print(elem)
            if elem > target:
                numbers.pop(i)
            elif elem == target and 0 not in numbers:
                numbers.pop(i)
            else:
                indexes.append(i+1)
        # print(numbers)
        return sorted(indexes)


print(Solution().twoSum(numbers = [1,2,3,4], target = 3))
