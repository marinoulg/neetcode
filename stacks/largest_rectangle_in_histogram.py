class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
            You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
        """
        # 1. Check (max) height

        # 2. Check (max) width

        # 3. Check (max) rectangle
            # by checking each column inidividually against the next one:
                # if the next one has only 1 block in common, drop the first column
                # if the next one more than 1 block in height, check this one against its next one to see if they share some height
                # Attention: ⚠️ important, it's a stack exercise, so drop unuseful columns
