import spisok
n = int(input('Кол-во чисел в массиве: '))
a = stas.massiv(n)
print(a)
a.append(9)
c = a.count(0)
f = a.count(1)
print()
print('Вероятность нуля: ', c/len(a))
print('Вероятность единицы: ', f/len(a))
maxim = 0
k = 1
b = []
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        k += 1
        maxim = max (maxim, k)
    else:
        b.append(k)
        k = 1
print(); print(b); print()
for j in range(2, maxim + 1):
    print('Вероятность', j, 'идущих подряд одинаковых эл-ов: ', b.count(j)/abs(len(a)-j))