class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = list()
        res = [0] * len(T)
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)

        return res
