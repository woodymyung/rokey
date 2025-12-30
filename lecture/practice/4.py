def frange(start, stop, step): 
    # start + step < stop 까지만 작동 
    while True: 
        if start + step >= stop: 
            raise StopIteration
        result = start
        start += step
        yield result

# def frange(start, stop, step): 
#     # start + step < stop 까지만 작동 
#     if start + step >= stop: 
#         raise StopIteration
#     result = start
#     start += step
#     yield round(result)


answer = frange(0.5, 1.0, 0.1)
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer))
print(next(answer))

