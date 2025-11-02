# map

nums = [1, 2, 3, 4, 5]


def double(x):
    return x*2

result = map(double, nums)

print(list(result))