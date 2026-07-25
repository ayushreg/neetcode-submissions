class TimeMap:

    def __init__(self):
        self.dataBase = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.dataBase):
            self.dataBase[key] = []
        self.dataBase[key].append([value, timestamp])    # at key =alice [[happy, 2], [sad, 3]] etc..
 
    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.dataBase):
            return ""

        value = self.dataBase[key]
        prev = ""
        for val in value:
            if(val[1] == timestamp):
                return val[0]
            
            if(val[1] > timestamp):
                return prev
            prev = val[0]

        return prev

        

