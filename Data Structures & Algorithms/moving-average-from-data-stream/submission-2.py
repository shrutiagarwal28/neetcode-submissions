class MovingAverage:

    def __init__(self, size: int):
        self.win_size = size
        self.window = deque()
        self.win_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.win_sum += val

        if len(self.window) > self.win_size:
            self.win_sum -= self.window.popleft()

        return self.win_sum / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
