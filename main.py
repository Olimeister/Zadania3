#Filip Olender

print("Zadanie1")
A = [1 - x for x in range(1, 11)]
B = [4 ** x for x in range(8)]
C = [x for x in B if x % 2 == 0]

print(u'Zbiór A: ', A, u'Zbiór B: ', B, u'Zbiór C: ', C)

print("Zadanie2")
from random import *

list1 = []
for element in range (10):
    random_nr = randrange(0,999)
    (list1.append(random_nr))
even_list = [x for x in list1 if x % 2 == 0]
print(even_list)

print("Zadanie3")
product_list = {'czekolada' : 'szt', 'cukierki' : 'kg', 'pączek' : 'szt', 'mleko' : 'litr', 'chleb' : 'szt'}
product_list1 = [keys for keys, values in product_list.items()]
product_list2 = [keys for keys, values in product_list.items() if values == 'szt']
print('Wszystkie produkty:', product_list1)
print('Produkty których wartości to sztuki: ',product_list2)



print("Zadanie6")
def ciag(list = [], a = 1, b = 4, ile = 10):
    x = 1
    for index in range(0, ile):
        x = x*b
        list.insert(index, x)
    list.insert(0, a)
    return list

print(ciag())



print("Zadanie7")
def ciag(*arguments):
    if len(arguments) == 1:
        return 0
    else:
        list = []
        x = 1
        for index in range(0, arguments[3]):
            x = x*arguments[2]
            list.insert(index, x)
        list.insert(0, arguments[1])
        return list
print(ciag(1, 1, 4, 10))


print("Zadanie8")
def product_list(**items):
    products = len(items.keys())
    price = sum(items.values())
    return products, price
total_price = product_list(czekolada=2.5, cukierki=3, pączek=1.5, mleko=4, chleb=3.5)
print(total_price)



print("Zadanie10")
from random import *

list = []
for number in range (20):
    random_nr = randrange(0,999)
    (list.append(random_nr))
list = [x for x in list if x % 4 == 0]

file = open('lab3.txt', 'w+')
file.write('Liczby podzielne przez 4:\n')
for number in list:
    file.writelines('[' + str(number) + ']')
file.close()

print("Zadanie11")
file = open('lab3.txt', 'r')
list = file.readlines()
for number in list:
    print(number)
file.close()