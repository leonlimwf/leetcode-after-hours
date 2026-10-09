class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        n = len(temperatures)
        # Initialize result array with zeros
        result = [0] * n

        for i in range(n):
            current = temperatures[i]
            while stack and temperatures[stack[len(stack)-1]] < current:
                prevIdx = stack.pop()
                result[prevIdx] = i - prevIdx
            stack.append(i)
        return result
