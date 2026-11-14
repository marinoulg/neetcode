from string import ascii_lowercase, punctuation
from pprint import pprint

class Solution:

    def encode(self, strs: list[str]) -> str:
        def dict_encode(strs):
            all_poss_strgs = []
            for elem in ascii_lowercase:
                all_poss_strgs.append(elem)

            for elem in punctuation:
                all_poss_strgs.append(elem)

            all_poss_strgs.append(" ")

            encoding_dict = {}
            for i in range(len(all_poss_strgs)):
                encoding_dict[all_poss_strgs[i]]=i+5*12

            return (encoding_dict)

        encoding_dict = dict_encode(strs)

        encoded_strs = []
        for elem in strs:
            for char in elem:
                encoded_strs.append(str(encoding_dict[char]))
            encoded_strs.append(str(encoding_dict[" "]))

        return "-".join(encoded_strs)


    def decode(self, s: str) -> list[str]:
        def dict_decode(strs):
            all_poss_strgs = []
            for elem in ascii_lowercase:
                all_poss_strgs.append(elem)

            for elem in punctuation:
                all_poss_strgs.append(elem)

            decoding_dict = {}
            for i in range(len(all_poss_strgs)):
                decoding_dict[i+5*12]=all_poss_strgs[i]

            return (decoding_dict)
        decoding_dict = dict_decode(strs)
        return decoding_dict



strs = ["hello", "how", "are", "you", "?"]

print(Solution().encode(strs))
