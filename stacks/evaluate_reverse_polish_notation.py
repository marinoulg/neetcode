class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        def turning_elems_in_order(tokens):
            tok = [tokens[0]]
            for i in range(1, len(tokens)):
                if i%2 == 0:
                    tok.insert(i-1,tokens[i])
                else:
                    tok.append(tokens[i])

            tok = (" ".join((tok)).split())
            # print("tok", tok)
            # print()
            return tok

        def turning_ints(tok):
            operators = ['+', '-', '*', '/']
            tok_integers = []
            for i in range(len(tok)):
                elem = tok[i]
                if elem not in operators:
                    tok_integers.append(int(elem))
                else:tok_integers.append((elem))

            # print("tok_integers",tok_integers)
            # print()
            return tok_integers

        def make_calculations(tok_integers):
            copy_tmp = []
            for elem in tok_integers:
                if elem in ["+", "-", "/", "*"]:
                    right = copy_tmp.pop(-1)
                    left = copy_tmp.pop(-1)
                    if elem == "+":
                        res = (left+right)
                        print(f"{left}+{right}")
                        copy_tmp.append(res)
                    elif elem == "-":
                        res = (left/right)
                        print(f"{left}-{right}")
                        copy_tmp.append(res)
                    elif elem == "*":
                        res = (left*right)
                        print(f"{left}*{right}")
                        copy_tmp.append(res)
                    elif elem == "/":
                        res = (left/right)
                        print(f"{left}/{right}")
                        copy_tmp.append(res)
                elif isinstance(elem, int):
                    copy_tmp.append(elem)

            res = copy_tmp[0]
            print("res:", res)
            return res

        def result(tokens):
            return int(make_calculations(turning_ints(turning_elems_in_order(tokens))))

        return result(tokens)


# tokens = ["1","2","+","3","*","4","-"]
# tokens=["4","13","5","/","+"]

tokens=["4","13","5","/","+"]

print(Solution().evalRPN(tokens))
