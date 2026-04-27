class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data = self.data[:-1]        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        mindata = min(self.data)
        return mindata
        
