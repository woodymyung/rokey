class CyclicIterator: 
    def __init__(self, data):
        self.data = data
        self.position = 0 
    
    def __iter__(self):
        return self 
    
    def __next__(self): 
        if self.position + 1 >= len(self.data): 
            self.position = self.position % 3
            result = self.data[self.position]
            self.position += 1
            return result
        result = self.data[self.position]
        self.position += 1
        return result

data = ['A', 'B', 'C']
iter = CyclicIterator(data)

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
