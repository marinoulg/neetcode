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

        def make_calculations(tok_integers, i, first):
            if tok_integers[i-1] == "+":
                # print("res", first + tok_integers[i])
                res = first + tok_integers[i]

            elif tok_integers[i-1] == "*":
                # print("res", first * tok_integers[i])
                res = first * tok_integers[i]

            elif tok_integers[i-1] == "-":
                # print("res", first - tok_integers[i])
                res = first - tok_integers[i]

            elif tok_integers[i-1] == "/":
                # print("res", first / tok_integers[i])
                res = first / tok_integers[i]

            return res

        def result(tokens):
            """
            ⚠️⚠️⚠️
            TO BE UPDATED

            https://en.wikipedia.org/wiki/Reverse_Polish_notation

            it works when operators are in the middle of the array
                --> when you need to operate from left to right without parentheses

            it does NOT work when:
                - operators are all at the end
                - operators are all around
            """

            tok = turning_elems_in_order(tokens)
            tok_integers = turning_ints(tok)

            first = tok_integers[0]
            for i in range(1, len(tok_integers)):
                if i%2==0:
                    if i == 2:
                        res = make_calculations(tok_integers, i, first)

                    else:
                        res = make_calculations(tok_integers, i, res)

            return (res)
        return result(tokens)


tokens = ["1","2","+","3","*","4","-"]

print(Solution().evalRPN(tokens))
