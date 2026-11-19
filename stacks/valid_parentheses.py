class Solution:
    def isValid(self, s: str) -> bool:
        # print(s)
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
                # print(idx, list_s[idx], "--> ", end="")
                list_s.pop(idx)
                idx -= 1
                # print("".join(list_s))

            return ("".join(list_s))

        def imbriqués(s):
            """
            works if imbriqués les uns dans les autres
            """
            s = clean_up_consecutives(s)
            # print("\npost cleanup:",s)

            opened = []
            closed = []

            parenth = 0
            bracket = 0
            curly = 0

            for idx in range(len(s)):
                elem = s[idx]
                # print(elem, ": ", end = "\n")
                if elem in ["[", "{", "("]:
                    # untangle_closed_open
                    opened.append(elem)
                    if elem == "(":
                        parenth += 1
                    elif elem == "{":
                        curly += 1
                    elif elem == "[":
                        bracket += 1

                if elem in ["]", ")", "}"]:
                    closed.append(elem)
                    # untangle_closed_open
                    if elem == ")":
                        parenth -= 1
                    elif elem == "}":
                        curly -= 1
                    elif elem == "]":
                        bracket -= 1

                # untangle_closed_open
                if parenth < 0 or curly < 0 or bracket < 0:
                    return False

                if len(closed) > len(opened):
                    return False

            # print("open:", opened)
            # print("closed:", closed)

            parallel_parenth = ")"
            parallel_bracket = "]"
            parallel_curly = "}"

            if len(opened) != len(closed):
                return False

            for op, clos, idx in zip(opened, closed[::-1], range(len(opened))):
                # print("index —", idx, end=": ")
                # print(op, clos)
                if op == "(" and clos != parallel_parenth:
                    # print("a")
                    return False
                if op == "[" and clos != parallel_bracket:
                    # print("b")
                    return False
                if op == "{" and clos != parallel_curly:
                    # print("c")
                    return False

            return True

        #  how to know how many times to do the cleanup? --> solved below
        if imbriqués(s) == False:
            # print("here:", s)
            s = clean_up_consecutives(s)
            if imbriqués(s) == False:
                return False
            else: return True
        else:
            return imbriqués(s)









# s = "([{}])" #should_true
# s = "[(])" #should_False
s="({()[()][{()}]})" #should_true
# s="(){}}{" #should_False
# s="(}{)" #should_False¨-

# s="{[()()]([])}" #should_true



print(Solution().isValid(s))
