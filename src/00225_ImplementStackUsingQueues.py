import queue

class MyStack:
    def __init__(self):
        self.queue = queue.Queue() 

    def push(self, x: int) -> None:
        self.queue.put(x) 

    def pop(self) -> int:
        size = self.queue.qsize()
        if size == 0:
            return None
        if size == 1:
            return self.queue.get()

        for i in range(size-1):
            temp = self.queue.get()
            self.queue.put(temp)

        lastItem = self.queue.get()
        return lastItem

    def top(self) -> int:
        size = self.queue.qsize()
        if size == 0:
            return None
        if size == 1:
            onlyItem = self.queue.get()
            self.queue.put(onlyItem)
            return onlyItem

        for i in range(size-1):
            temp = self.queue.get()
            self.queue.put(temp)

        lastItem = self.queue.get()
        self.queue.put(lastItem)

        return lastItem

    def empty(self) -> bool:
        return self.queue.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()