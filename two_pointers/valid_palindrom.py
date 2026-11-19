from string import punctuation

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        for elem in s:
            if elem in punctuation:
                s = s.replace(elem,"")

        if (s) == (s[::-1]):
            return True
        else: return False



s = "Was it a car or a cat I saw?"
print(Solution().isPalindrome(s))
