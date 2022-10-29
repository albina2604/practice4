with open('task1.txt', 'w') as file:
    n = list(map(float, input('Ведите числа - ').split()))
    for i in range(len(n)):
        file.write(str(n[i]) + '\n')
