class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        tok_integers = []
        for elem in tokens:
            if elem in ["+", "-", "*", "/"]:
                tok_integers.append(elem)
            else: tok_integers.append(int(elem))

        copy_tmp = []
        for elem in tok_integers:
            if elem in ["+", "-", "/", "*"]:
                right = copy_tmp.pop(-1)
                left = copy_tmp.pop(-1)
                if elem == "+":
                    res = int(left+right)
                    print(f"{left}+{right}={res}")
                    copy_tmp.append(res)
                elif elem == "-":
                    res = int(left-right)
                    print(f"{left}-{right}={res}")
                    copy_tmp.append(res)
                elif elem == "*":
                    res = int(left*right)
                    print(f"{left}*{right}={res}")
                    copy_tmp.append(res)
                elif elem == "/":
                    res = int(left/right)
                    print(f"{left}/{right}={res}")
                    copy_tmp.append(res)
            elif isinstance(elem, int):
                copy_tmp.append(elem)
        res = (copy_tmp)[0]
        print("res:", res)

        return int(res)


# tokens = ["1","2","+","3","*","4","-"]
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


print(Solution().evalRPN(tokens))
