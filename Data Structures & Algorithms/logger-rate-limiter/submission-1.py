class Logger:

    def __init__(self):
        self.last_print = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_print:
            self.last_print[message] = timestamp + 10
            return True
        else:
            if timestamp < self.last_print[message]:
                
                return False
            self.last_print[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
