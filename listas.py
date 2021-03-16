#Loops en listas


my_list = list(range(100))
pares = [i for i in my_list if i%3 ==0]
print(pares)


print('\n\n')


double = [i*2 for i in my_list ]
print(double)
