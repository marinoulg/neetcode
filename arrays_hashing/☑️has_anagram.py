class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list()
        for elem in s:
            list_s.append(elem)
        list_t = list()
        for elem in t:
            list_t.append(elem)
        list_s.sort()
        list_t.sort()
        if (list_s) == (list_t):
            return True
        else: return False
