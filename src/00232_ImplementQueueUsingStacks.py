class MyQueue:

    def __init__(self):
        # Initializing two Stack. stack1 and stack2
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Appending the value to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # Same expaination as pop
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check the length of both the stack and return the answer.
        return len(self.stack1) == 0 and len(self.stack2) == 0