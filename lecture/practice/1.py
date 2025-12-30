class ReverseIterator: 
    def __init__(self, data): 
        self.data = data 
        self.position = len(data) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0: 
            print('StopIteration')
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
            

data = [1, 2, 3, 4]
iter = ReverseIterator(data)

for i in iter:
    print(i)