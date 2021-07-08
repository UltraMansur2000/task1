percent = int(input('Введите число для склонения со словом проценты:'))
if percent % 10 == 1 and percent % 100 != 11:
    print(f'{percent} процент')
elif percent % 10 == 0:
    print(f'{percent} процентов')
elif percent % 10 <= 4 and percent % 100 // 10 != 1:
    print(f'{percent} процента')
else:
    print(f'{percent} процентов')
