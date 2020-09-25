from functools import reduce
x = 'computer'
print(x[1:8:6])
y = [1,2,3]
for index, value in enumerate(y):
    print(index, value)

z = lambda y : y*2

print(list(map(lambda y : y*2 , y)))
print([value*2 for value in y])
print(list(filter(lambda y : y >= 2, y)))
print([value >= 2 for value in y])
print([value for value in y if value >= 2])


for i in range(1, 10):
    print(i, end=' ')

print(reduce(lambda x,z: x*z, y))


print()