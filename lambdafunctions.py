def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

mapped_list = list(map(lambda num : num % 2, numbers_list))
print(mapped_list)

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5,6))

z = lambda a,b,c : a + b + c
print(z(5,6,2))