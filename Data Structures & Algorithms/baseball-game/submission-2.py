class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()
        for i in range(len(operations)):
            if operations[i] == '+':
                temp = operations[i-1] + operations[i-2]
                stack.push(temp)
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                temp = int(operations[i-1]) * 2
                stack.push(temp)
            else:
                stack.push(int(operations[i]))
        return stack.total()
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def show_stack(self):
        for i in self.stack:
            print(i)
    def total(self):
        return (sum(self.stack))