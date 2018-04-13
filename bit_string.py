class BitString(object):
    def __init__(self, len):
        self.len = len
        self.max = 2**len
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.max:
            cur, self.num = self.num, self.num+1
            result = [0 for i in range(self.len)]
            for i in range(self.len):
                result[i] = cur % 2
                cur = int(cur/2)
            return result
        else:
            raise StopIteration()
