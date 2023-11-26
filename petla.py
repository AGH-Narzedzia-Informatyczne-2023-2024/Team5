def fun(n):
    return n*n + 3*n + 4

print("Podaj ilości liczb")
n = int(input())

for i in range(0, n):
    print(fun(i))
