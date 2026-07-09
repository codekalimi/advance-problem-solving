class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_scores = []
        result = 0
        for i in range(len(operations)):
            if operations[i] == '+':
                val = (final_scores[-1] + final_scores[-2])
                final_scores.append(val)
            elif operations[i] == 'C':
                final_scores.pop()
            elif operations[i] == 'D':
                val = (final_scores[-1] * 2)
                final_scores.append(val)
            else:
                val = int(operations[i])
                final_scores.append(val)
        result = sum(final_scores)
        return result