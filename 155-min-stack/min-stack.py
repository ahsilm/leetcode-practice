class MinStack:

    def __init__(self):
        self.stack= []
    
    def push(self, val: int) -> None:
        self.stack.append(val)    

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minStackArr = []
        minStackArr.append(self.stack[-1])
        for el in self.stack:
            minimum = minStackArr[-1]
            if el < minimum:
                minStackArr.append(el)
            else:
                continue
        return minStackArr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()