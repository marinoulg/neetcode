class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        counts = []

        sorted_temp = sorted(list(set(temperatures[:])), reverse=True)
        # print(sorted_temp)
        counts = []
        if len(sorted_temp) == 1:
            for i in range(len(temperatures)):
                counts.append(0)
            return counts

        # print()
        for i in range(len(temperatures)):
            t_tmp = temperatures[i]
            # print(t_tmp, end=": ")
            count = 0
            for elem in temperatures[i+1:]:
                sorted_temp = sorted(list(set(temperatures[i+1:])), reverse=True)
                # print(sorted_temp)
                if sorted_temp[0] > t_tmp:
                    if elem > t_tmp:
                        count += 1
                        # print(count)
                        counts.append(count)
                        break
                    else:
                        count += 1
                        # sorted_temp.pop(0)
                else:
                    count = 0
                    counts.append(count)
                    sorted_temp.pop(0)
                    # print(count)
                    break
                # print(count, end=" —> ")
                sorted_temp.remove(elem)

            if i == len(temperatures)-1:
                ""
                # print(0)
            # print()

        if len(temperatures) > len(counts):
            counts.append(0) # because the last one is always 0
            # print(count)

        return counts

temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

print(Solution().dailyTemperatures(temperatures))
