from typing import List


class Solution:
    # brute force solution, time limit exceed
    def dailyTemperatures_tle(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i in range(len(temperatures)):
            stack = []
            for j in range(i, len(temperatures)):
                if temperatures[i] >= temperatures[j]:
                       stack.append(temperatures[j])
                else:
                       break
            if len(stack) == len(temperatures) - i and stack[-1] <= temperatures[i]:
                stack = []
            answer.append(len(stack))
        return answer

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for x in range(len(temperatures))]
        stack = [(0, temperatures[0])]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j = stack.pop()[0]
                answer[j] = i - j
            stack.append((i, temp))
        return answer
