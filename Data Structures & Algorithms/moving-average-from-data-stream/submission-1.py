class MovingAverage:

    def __init__(self, size: int):
        self.win_size = size
        self.window = deque()
        self.win_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.count += 1
        tail = self.window.popleft() if self.count > self.win_size else 0
        
        self.win_sum = self.win_sum - tail + val
        return self.win_sum / min(self.win_size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
