from tkinter import N


def task2():
    '''
    Решение к задаче 2
    Arg:
    n - числа, введенные пользователем

    Result:
    сумма и максимум - 'task2.txt'
    '''
    n = list(map(float, input('Ведите числа - ').split()))
    with open('task2.txt', 'w', encoding='UTF-8') as file:
        for i in range(len(n)):
            file.write(str(n[i]) + '\n')
        file.write(f'{sum(n):.2f}\n{max(n):.2f}')
        return n


task2()
