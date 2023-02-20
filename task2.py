number = int(input("введите количество элементов массива"))
massiv = [int(input("введите элемент массива:  ")) for i in range(number)]
indexes = []
print(massiv)
min = int(input("введите минимум диапазона"))
max = int(input("введите максимум диапазона"))
for k in range(len(massiv)):
    if max>=massiv[k]>=min:
        indexes.append(k)
print(indexes)
