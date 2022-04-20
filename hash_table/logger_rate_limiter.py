class Logger:

    def __init__(self):
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        self.message_timestamp.setdefault(message, 0)
        if timestamp >= self.message_timestamp[message]:
            self.message_timestamp[message] = timestamp + 10
            return True
        return False
