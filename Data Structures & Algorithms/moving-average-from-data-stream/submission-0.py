class MovingAverage:

    def __init__(self, size: int):
        self.win_size = size
        self.window = deque()

    def next(self, val: int) -> float:
        if len(self.window) >= self.win_size:
            self.window.popleft()

        self.window.append(val)
        avg = sum(self.window)/len(self.window)
        return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
