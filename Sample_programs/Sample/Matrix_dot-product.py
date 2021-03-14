# dot product
xvec = [10, 20, 30]
yvec = [9, 1, 3]
x = sum(x*y for x, y in zip(xvec, yvec))
print(x)