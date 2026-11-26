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
        print("------")

        # 3. Check (max) rectangle
            # by checking each column inidividually against the next one:
                # if the next one has only 1 block in common, drop the first column
                # if the next one more than 1 block in height, check this one against its next one to see if they share some height
                # Attention: ⚠️ important, it's a stack exercise, so drop unuseful columns

        # def minis_to_use(heights):
        #     return [elem-1 for elem in heights]

        def try_with_min(min_cons, consecutives):
            # print(min_cons)
            print("consecutives:", consecutives)

            cons_copy = []
            if consecutives != []:
                for i in reversed(range(1, len(consecutives))):
                    elem = consecutives[i]
                    next_ = consecutives[i-1]
                    print(elem, next_)
                    if elem >= min_cons and next_ >= min_cons:
                        cons_copy.append(min_cons)

                next_ = consecutives[1]
                print("next:", next_)

                if next_ >= min_cons:
                    cons_copy.append(min_cons)

                if cons_copy != []:
                    max_rectangle = cons_copy[0]*len(cons_copy)
                    print("\ncons_copy:",cons_copy)
                    print("max_rectangle:",max_rectangle)
                    return max_rectangle
                else: return 0

            else: return 0

        def try_for_1_mini(heights, mini):
            """
            if mini = 1
            je coupe à 2
            --> plus logique
            """
            if mini != 0:
                for i in range(len(heights)):
                    elem = heights[i]
                    if i == 0:
                        left = []
                    if i == len(heights):
                        right = []
                    # if elem == heights[-1]:
                    #     right = []
                    elif elem == mini:
                        left = heights[:i+1]
                        right = heights[i:]
                        print(left, right)
            # elif mini not in heights:
            #     for elem in heights:
            #         if elem >= mini:


            else:
                left = heights
                right = []


            try_left = try_with_min(mini+1, left)
            try_right = try_with_min(mini+1, right)
            print(try_left if try_left > try_right else try_right)

            return try_left if try_left > try_right else try_right

        tmp_res = []
        # minis = sorted(set(minis_to_use(heights)))
        # minis.remove(0)
        # print(minis)

        # for elem in minis:
        #     print("elem", elem)
        #     res = try_for_1_mini(heights, elem)
        #     # print("elem, res:", elem, res)
        #     tmp_res.append(res)


        # print(tmp_res)
        # max_rectangle = max(tmp_res)


        # if max_height_width < max_rectangle:
        #     return max_rectangle
        # else:
        #     return max_height_width
        # print(try_for_1_mini(heights, 1))
        print(try_with_min(4, [7, 1, 7, 2, 2, 4]))



print(Solution().largestRectangleArea(heights = [7,1,7,2,2,4])) # expect 8
# print()
# print(Solution().largestRectangleArea(heights = [1,3,7])) # expect 7
# print()
# print(Solution().largestRectangleArea(heights=[2,1,5,6,2,3])) # expect 10
