a = dict()
n = int(input("Enter size of dictionary: "))
for i in range(n):
    x = input("Enter key: ")
    y = input("Enter value: ")
    a[x] = y
print("Second largest value: ", list(sorted(a.values()))[-2])

# Code by shreyansh sharma