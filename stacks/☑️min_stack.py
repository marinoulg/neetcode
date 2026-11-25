class MinStack:
    def __init__(self):
        self.stack = []
        self.output = [None]
        self.mini = -2**32 # below the range in exercise for self.mini
        return None

    def push(self, val: int) -> None:
        self.stack.insert(len(self.stack), val)
        self.output.append(None)
        if self.mini == -2**32:
            self.mini = val
        else:
            if val <= self.mini:
                self.mini = val
        return None

    def pop(self) -> None:
        self.stack.pop(-1)
        self.output.append(None)
        return None

    def top(self) -> int:
        self.output.append(self.stack[-1])
        return self.stack[-1]

    def getMin(self) -> int:
        if self.mini in self.stack:
            self.output.append(self.mini)
        else:
            mini = self.stack[0]
            for elem in self.stack:
                if elem <= mini:
                    mini = elem
            self.mini = mini
            self.output.append(self.mini)
        return self.mini

input_ = ["MinStack", "push", 2147483647, "push", 2147483647, "push", -2147483648,
          "getMin", "pop", "getMin", "pop", "getMin"]

def running_input(input_):
    for i in range(len(input_)):
        elem = input_[i]
        if elem == "MinStack":
            minStack = MinStack()
        elif elem == "push":
            minStack.push(input_[i+1])
            i+=2
        elif elem == "getMin":
            minStack.getMin()
        elif elem == "pop":
            minStack.pop()
        elif elem == "top":
            minStack.top()
        print(minStack.stack)

    return (minStack.output)
print(running_input(input_))
