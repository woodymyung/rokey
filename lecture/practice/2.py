def fib_generator(): 
    i = 1
    result = 1
    while True: 
        if i == 1 or i == 2: 
            i = i+1
            yield result
        else: 
            result = (i-1) + (i-2)
            i = i+1
            yield result

g = fib_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))