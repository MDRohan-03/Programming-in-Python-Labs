N = int(input("Enter: "))

a = 0
b = 1

for i in range(N):
    print(a)
    c = a + b
    a = b
    b = c