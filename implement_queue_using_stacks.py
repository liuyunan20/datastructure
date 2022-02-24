class MyQueue:

    def __init__(self):
        self.my_queue = []

    def push(self, x: int) -> None:
        self.my_queue.append(x)

    def pop(self) -> int:
        pop_element = self.my_queue[0]
        self.my_queue.remove(self.my_queue[0])
        return pop_element

    def peek(self) -> int:
        return self.my_queue[0]

    def empty(self) -> bool:
        if len(self.my_queue) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
