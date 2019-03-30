my_items = ["h", 'i', 'h']
for i, item in enumerate(my_items):
    print(f'{i}: {item}')


emails = {
    'Боб': 'bob@example.com',
    'Алиса': 'alice@example.com',
}
for name, email in emails.items():
    print(f'{name} -> {email}')

'''
range() — она принимает необязательные параметры, которые
управляют начальным значением ( a ), конечным значением ( n ) и размером
шага ( s ) цикла. Перевод с Java на Python будет выглядеть так:
for i in range(a, n, s):
    '''
even_squares = [x * x for x in range(10) if x % 2 == 0]