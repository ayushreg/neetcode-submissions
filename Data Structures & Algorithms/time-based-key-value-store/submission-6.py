class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)  # creates a [] at each key

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.hashMap):
            return ""

        pairList = self.hashMap[key]  # [[alic,2], [jake,3]]
        l = 0
        r = len(pairList) - 1

        while(l <= r):
            mid = (l + r) // 2

            if(pairList[mid][1] == timestamp):
                return pairList[mid][0]
            elif(pairList[mid][1] > timestamp):
                r = mid - 1
            else:
                l = mid + 1

        if(pairList[r][1] > timestamp):
            return ""
        else:
            return pairList[r][0]
