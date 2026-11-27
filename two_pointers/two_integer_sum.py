class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ""
        # indexes = []
        # keep_track_idx = {}

        # for idx in range(len(numbers)):
        #     if numbers[idx] not in keep_track_idx:
        #         keep_track_idx[numbers[idx]] = [idx+1]
        #     else: keep_track_idx[numbers[idx]].append(idx+1)

        # print(keep_track_idx)
        # numbers = (sorted(numbers))
        if len(numbers)%2 == 0: middle = int(len(numbers)/2)
        else: middle = int(len(numbers)/2)+1
        # print("middle", middle)

        possibles = []
        for idx_forward, idx_backwards in zip(range(len(numbers)), reversed(range(len(numbers)))):
            # print(idx_forward, idx_backwards)
            if 0 in numbers:
                if idx_forward <= middle and idx_backwards >= middle:
                    if numbers[idx_forward] <= target:
                        possibles.append(numbers[idx_forward])
                    if numbers[idx_backwards] <= target:
                        possibles.append(numbers[idx_backwards])
                else: break
            else:
                if idx_forward <= middle and idx_backwards >= middle:
                    if numbers[idx_forward] <= target:
                        possibles.append(numbers[idx_forward])
                    if numbers[idx_backwards] < target:
                        possibles.append(numbers[idx_backwards])
                else: break

        return (possibles)


print(Solution().twoSum(numbers = [1,2,3,4], target = 3))
