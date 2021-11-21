class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Correct Answer
# class MyQueue:

#     def __init__(self):
#         self.stack = []
#         self.ready_to_out = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         self.peek()
#         return self.ready_to_out.pop()

#     def peek(self) -> int:
#         if not self.ready_to_out:
#             while self.stack:
#                 self.ready_to_out.append(self.stack.pop())
#         return self.ready_to_out[-1]

#     def empty(self) -> bool:
#         return not self.stack and not self.ready_to_out

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()