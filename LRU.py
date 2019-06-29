    def __init__(self, capacity: int):
        self.d = collections.OrderedDict()
        self.c = capacity

    def get(self, key: int) -> int:
        ret = -1
        if key in self.d:
            ret, self.d[key] = self.d[key], self.d.pop(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
        self.d[key] = value
        if len(self.d) > self.c:
            self.d.popitem(last=False)