z = "python"
y = list(z[i] for i in range (len(z)))
x = list(z[i] for i in range(len(z)-1, -1, -1))
print(y)
print(x)