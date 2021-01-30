def mult2(n):
    return n * 2

print(mult2(10))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2

mult2_list(numbers)

print(numbers)

