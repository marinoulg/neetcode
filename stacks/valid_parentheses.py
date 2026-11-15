class Solution:
    def isValid(self, s: str) -> bool:
        # print(s)
        def pair(s):
            """
            this creates a dict whose key is the first idx of first char,
            and whose value is the according tuple (parenthesis, bracket, curly)
            """

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
            """
            ⚠️⚠️⚠️
            TO BE UPDATED

            a round is when:
                - either it finishes (as it is now) --> ends in (0,0,0)
                - or when, while in a round, a subround opens up (and closes) --> to be implemented
            """

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

        all_parentheses = []
        all_brackets = []
        all_curly = []
        for tupl in r:
            all_parentheses.append(tupl[0])
            all_brackets.append(tupl[1])
            all_curly.append(tupl[2])

        # print(all_parentheses)
        # print(all_brackets)
        # print(all_curly)

        def check_all_in_order(all_p):
            """
            if one starts off in a closed way instead of an open one,
            it gets returned False right away
            """

            for elem in all_p:
                # print(elem)
                if elem <0:
                    return False
            else: return True

        if check_all_in_order(all_parentheses) and \
            check_all_in_order(all_curly) and \
                check_all_in_order(all_brackets):
            """
            we are sure it never starts off in a closed way
            """

            if r[-1] == (0,0,0):
                """
                we know it finishes all even (all that was open is now closed)
                """

                idx=0
                i = 0
                tmp, idx, nb_zeros = closed_rounds(r, idx)
                all_rounds = [tmp]

                while i != nb_zeros+1:
                    """
                    ⚠️⚠️⚠️
                    we are creating the subrounds, based only on the criteria
                    that a round is finished when it is all closed

                    TO BE UPDATED
                    """

                    tmp, idx, nb_zeros = closed_rounds(r, idx)
                    all_rounds.append(tmp)
                    i += 1

                print(all_rounds)
                print()
                for array in all_rounds:
                    # print(array)
                    for elem in array:
                        if elem == (0,0,0):
                            array.remove(elem)
                            """
                            bc otherwise the alternate_r results in False when it should not
                            """

                    print(array)

                    if len(array) != 1:
                        """
                        once all "0" are out, if a round is composed of >1 elements,
                        we turn it upside down to verify if it is symmetrical

                        if it is not, the result must be False
                        """
                        alternate_r = array[::-1]
                        if alternate_r != array:
                            return False

                    # print()
                return True

            else: return False
        else: return False






s = "([{}])" #should_true
# s = "[(])" #should_False
# s="()[()]{}" #should_true
# s="(){}}{" #should_False
# s="(}{)" #should_False

# s="{[()()]([])}" #should_true



print(Solution().isValid(s))

# print((0,-1)>0)
