class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}
        test = []
        for word in strs:
            tmp = []
            for letter in word:
                tmp.append(letter)

            if "".join(sorted(tmp)) not in words:
                words["".join(sorted(tmp))] = [word]
            else: words["".join(sorted(tmp))].append(word)

        return (list(words.values()))
