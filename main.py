fe = 1
se = 1
n = input("Номер элемента последовательнocти ")
n = int(n)

print(fe, se, end=' ')
while n > 2:
    summa = fe + se
    fe = se
    se = summa
    print (summa, end=' ')
    n -= 1