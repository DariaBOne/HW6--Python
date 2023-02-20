n = int(input("введите кол-во элементов в маcсиве"))
a = int(input("введите первый элемент"))
d = int(input("введите разность"))
list = [a]
for i in range(2,n+1):
    element = a+(i-1)*d
    list.append(element)
print(list)

