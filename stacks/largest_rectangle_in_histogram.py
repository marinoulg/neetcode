class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
            You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
        """
        # 1. Check (max) height
        max_height = max(heights)
        print("max_height:", max_height)

        # 2. Check (max) width
        max_width = len(heights)
        print("max_width:", max_width)

        if max_height > max_width:
            max_height_width = max_height
        else:
            max_height_width = max_height

        print("max_height_width:", max_height_width)

        # 3. Check (max) rectangle
            # by checking each column inidividually against the next one:
                # if the next one has only 1 block in common, drop the first column
                # if the next one more than 1 block in height, check this one against its next one to see if they share some height
                # Attention: ⚠️ important, it's a stack exercise, so drop unuseful columns

        consecutives = []
        for i in range(len(heights)-1):
            col1 = range(heights[i]+1)
            col2 = range(heights[i+1]+1)
            print(col1, col2, end=": ")

            max_col1 = max(col1)
            max_col2 = max(col2)

            if max_col1 in col2:
                print(range(max_col1+1))
                consecutives.append(max_col1)
            elif max_col2 in col1:
                print(range(max_col2+1))
                consecutives.append(max_col2)


        # dealing with last_num
        last_num = range(heights[-1]+1)
        print(range(max_col2), last_num, end=': ')
        if max_col2 in last_num:
            consecutives.append(max_col2)
            print(range(max_col1+1))
        else:
            print(range(max(last_num)+1))
            consecutives.append(max(last_num))


        # max_cons = max(consecutives)
        for elem in consecutives[::-1]:
            if elem == 1:
                consecutives.remove(elem)

        min_cons = min(consecutives)
        print(min_cons)
        print("consecutives:", consecutives)

        cons_copy = []
        for elem in consecutives:
            if elem >= min_cons:
                cons_copy.append(min_cons)

        print(cons_copy)

        max_rectangle = cons_copy[0]*len(cons_copy)
        if max_height_width < max_rectangle:
            return max_rectangle
        else:
            return max_height_width




# print(Solution().largestRectangleArea(heights = [7,1,7,2,2,4]))
# print()
# print(Solution().largestRectangleArea(heights = [1,3,7]))
# print()
print(Solution().largestRectangleArea(heights=[2,1,5,6,2,3]))
