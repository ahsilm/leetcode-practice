class MinStack:

    def __init__(self):
        self.stack= []
        self.minStack = []
    
    def push(self, val: int) -> None: 
        self.stack.append(val)   
        if(len(self.minStack) == 0):
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        # lastidx = len(self.stack) - 1
        # minEl = self.stack[-1]
        # arr = [lastidx]
        # for i in range(0,len(self.stack)-1):
        #     currEl = self.stack[i]
        #     if currEl < minEl:
        #         minEl = currEl
        #         arr.append(i)
        #     else:
        #         continue

        # topidx = arr[-1]   
        # return(self.stack[topidx])
                




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()