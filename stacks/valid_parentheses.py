class Solution:
    def isValid(self, s: str) -> bool:
        print(s)

        def pair(s):
            rounds = {}
            c_p = 0
            c_bracket = 0
            c_curly = 0

            for i in range(len(s)):
                elem = s[i]
                if elem == "(":
                    c_p += 1
                elif elem == ")":
                    c_p -= 1

                elif elem == "{":
                    c_bracket += 1
                elif elem == "}":
                    c_bracket -= 1

                elif elem == "[":
                    c_curly += 1
                elif elem == "]":
                    c_curly -= 1

                rounds[i] = (c_p, c_bracket, c_curly)

            return rounds

        def closed_rounds(r, idx):
                        tmp = []
                        nb_zeros = 0
                        for i in range(idx, len(r)):
                            elem = r[i]

                            if elem != (0,0,0):
                                tmp.append(elem)
                                idx += 1
                            else:
                                nb_zeros += 1
                                tmp.append((0,0,0))
                                idx += 1
                                break

                        return tmp, idx, nb_zeros

        rounds = pair(s)
        r = list(rounds.values())

        if r[-1] == (0,0,0):
            idx=0
            i = 0
            tmp, idx, nb_zeros = closed_rounds(r, idx)
            all_rounds = [tmp]

            while i != nb_zeros+1:
                tmp, idx, nb_zeros = closed_rounds(r, idx)
                all_rounds.append(tmp)
                i += 1

            print(rounds)
            print()
            for array in all_rounds:
                print(array)
                for elem in array:
                    if elem == (0,0,0):
                        array.remove(elem)
                print(array)
                if len(array) != 1:
                    alternate_r = array[::-1]
                    if alternate_r != array:
                        return False
                else:
                    for elem in array[0]:
                        if elem == -1:
                            return False

                print()
            return True

        else: return False


# s = "([{}])"
# s = "[(])"
# s="()[()]{}"
# s="(){}}{"
s="(}{)"


print(Solution().isValid(s))

# print((0,-1)>0)
