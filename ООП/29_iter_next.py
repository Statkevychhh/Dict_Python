class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step
    
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
    
    def __iter__(self):
        self.value  = self.start - self.step
        return self

fr = FRange(0, 2, 0.5)
print(fr.__next__())
print(fr.__next__())
print(next(fr))
print(next(fr))
print()


for x in fr:
    print(x)
print()




# 2)
class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr2 = FRange(start, stop, step)
    
    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr2)
        else:
            raise StopIteration


fr2 = FRange2D(0, 2, 0.5, 4)
for row in fr2:
    for x in row:
        print(x, end=' ')
    print()