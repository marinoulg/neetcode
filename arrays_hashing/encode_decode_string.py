from string import ascii_lowercase, punctuation, ascii_uppercase
from pprint import pprint

class Solution:

    def encode(self, strs: list[str]) -> str:
        def dict_encode(strs):
            all_poss_strgs = []
            for elem in ascii_lowercase:
                all_poss_strgs.append(elem)
            for elem in ascii_uppercase:
                all_poss_strgs.append(elem)
            for elem in punctuation:
                all_poss_strgs.append(elem)

            all_poss_strgs.append(" ")

            encoding_dict = {}
            for i in range(len(all_poss_strgs)):
                encoding_dict[all_poss_strgs[i]]=i+5*12

            for elem in range(10):
                encoding_dict[str(elem)] = (ascii_lowercase[elem])

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
            for elem in ascii_uppercase:
                all_poss_strgs.append(elem)
            for elem in punctuation:
                all_poss_strgs.append(elem)
            # for elem in range(10):
            #     all_poss_strgs.append(ascii_lowercase[elem])

            all_poss_strgs.append(" ")

            decoding_dict = {}
            for i in range(len(all_poss_strgs)):
                decoding_dict[str(i+5*12)]=all_poss_strgs[i]

            # for elem in range(10):
            #     decoding_dict[(ascii_lowercase[elem])] =  str(elem)

            return (decoding_dict)

        decoding_dict = dict_decode(s)
        decoded_list = s.split("-")

        # pprint(decoding_dict)
        decoded_strs = []
        for elem in decoded_list:
            decoded_strs.append(decoding_dict[(elem)])

        return ''.join(decoded_strs).split(" ")[:-1]




strs = ["100"]

encoded = (Solution().encode(strs))
print("encoded:",encoded)
print()
# print(Solution().decode(encoded))
