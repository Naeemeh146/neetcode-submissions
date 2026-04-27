class MinStack:

    def __init__(self):
        self.data = []
        self.mindata = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        
        if self.mindata:
            if val <= self.mindata[-1]:
                self.mindata.append(val)
        else:
            self.mindata.append(val)

    def pop(self) -> None:
        num = self.data[-1]
        self.data = self.data[:-1]

        if self.mindata:
            if self.mindata[-1] == num:
                self.mindata.pop()
        
        


    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        
        return self.mindata[-1]
        
