class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = [0]
        size = len(temp)
        answer = [None] * size

        i = 1
        while(i < size):
            if temp[stack[-1]] < temp[i]:
                diff = i - stack[-1]
                answer[stack[-1]] = diff
                stack.pop(-1)
                if len(stack) != 0:
                    continue
            stack.append(i)
            # print(stack)
            i+=1
        while(len(stack)!= 0):
            answer[stack[-1]] = 0
            stack.pop(-1)
        return answer
         