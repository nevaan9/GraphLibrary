def euclidian(a,b):
    if a % b == 0:
        return b
    else:
        return euclidian(b, a%b)


list = [x for x in range(10)]
for i, m in enumerate(list):
    print(i, m)


for index, ch in enumerate("Nevaan"):
    print(index+1, ch)