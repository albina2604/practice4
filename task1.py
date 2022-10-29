def task1():
    '''
    Решение к задаче 1
    Arg:
    n - числа, введенные пользователем

    Result:
    новый файл - 'task1.txt' 
    '''
    n = list(map(float, input('Ведите числа - ').split()))
    with open('task1.txt', 'w', encoding='UTF-8') as file:
        for i in range(len(n)):
            file.write(str(n[i]) + '\n')
        return n


task1()
