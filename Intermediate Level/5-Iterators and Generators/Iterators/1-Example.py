#Example 1: Custom iterator for a range of numbers

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using the custom iterator
myrange = MyRange(1, 5)
for i in myrange:
    print(i)
