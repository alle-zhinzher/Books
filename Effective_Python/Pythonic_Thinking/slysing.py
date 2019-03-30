a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[4:]
print('Before:', b)
b[1] = 99
print('After:', b)
print('No change:', a)

b = a[:]
print(b == a)
assert b == a and b is not a
