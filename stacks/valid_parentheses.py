class Solution:
    def isValid(self, s: str) -> bool:
        def old():
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

        print(s)
        def clean_up_consecutives(s):
            """
            clean up first
            """
            to_drop = []
            for i in range(len(s)-1):
                elem = s[i]
                next_elem = s[i+1]
                # print(elem, next_elem)
                if elem == "(" and next_elem == ")":
                    to_drop.append(i)
                    to_drop.append(i+1)
                    i += 2
                elif elem == "{" and next_elem == "}":
                    to_drop.append(i)
                    to_drop.append(i+1)
                    i += 2
                elif elem == "[" and next_elem == "]":
                    to_drop.append(i)
                    to_drop.append(i+1)
                    i += 2

            # print(to_drop)

            list_s = (list(s))

            for idx in to_drop[::-1]:
                print(idx, list_s[idx], "--> ", end="")
                list_s.pop(idx)
                idx -= 1
                print("".join(list_s))

            s = ("".join(list_s))

            return s


        def untangle_closed_open(s):
            """
            TO DO
            """

            s = clean_up_consecutives(s)


            """if imbriqués(s) == False:
                s = clean_up_consecutives(s)
                if imbriqués(s) == False:
                    return False"""

            print("post cleanup:",s)


            return s



        def imbriqués(s):
            """
            works if imbriqués les uns dans les autres
            """
            s = untangle_closed_open(s)

            opened = []
            closed = []

            # idx_op = []
            # idx_clos = []

            for idx in range(len(s)):
                elem = s[idx]
                print(elem, ": ", end = "")
                if elem in ["[", "{", "("]:
                    opened.append(elem)
                    # idx_op.append(idx)
                if elem in ["]", ")", "}"]:
                    closed.append(elem)
                    # idx_clos.append(idx)
                # print("lenght opened:",len(opened), end=" — ")
                # print("lenght closed:", len(closed))
                if len(closed) > len(opened):
                    # here, does not return False because } closes when ) should close, and then { opens, and then ) closes
                    return False

            print("open:", opened)
            print("closed:", closed)

            parallel_parenth = ")"
            parallel_bracket = "]"
            parallel_curly = "}"

            # print("idx_op:", idx_op)
            # print("idx_clos:", idx_clos)

            if len(opened) != len(closed):
                return False

            for op, clos, idx in zip(opened, closed[::-1], range(len(opened))):
                print("index —", idx, end=": ")
                print(op, clos)
                if op == "(" and clos != parallel_parenth:
                    print("a")
                    return False
                if op == "[" and clos != parallel_bracket:
                    print("b")
                    return False
                if op == "{" and clos != parallel_curly:
                    print("c")
                    return False
                print()

            return True

        #  how to know how many times to do the cleanup? --> solved below
        if imbriqués(s) == False:
            print("here:", s)
            s = clean_up_consecutives(s)
            if imbriqués(s) == False:
                return False
            else: return True
        else:
            return imbriqués(s)









# s = "([{}])" #should_true
# s = "[(])" #should_False
# s="({()[()][{()}]})" #should_true
s="(){}}{" #should_False
s="(}{)" #should_False

# s="{[()()]([])}" #should_true



print(Solution().isValid(s))
