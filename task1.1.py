time = int(input('Введите время: '))
min = 60
hour = min * 60
day = hour * 24
month = day * 30
year = month * 12
if time // 60 == 0:
    print(f'{time} сек')
elif time // min < 60:
    m = time // min
    s = time % 60
    print(f'{m} мин {s} сек')
elif time // hour < 24:
    h = time // hour
    m = time % hour // min
    s = time % 60
    print(f'{h} час {m} мин {s} сек')
elif time // day < 30:
    d = time // day
    h = time % day // hour
    m = time % day % hour // min
    s = time % 60
    print(f'{d} ден {h} час {m} мин {s} сек')
elif time // month < 12:
    mon = time // month
    d = time % month // day
    h = time % month % day // hour
    m = time % month % day % hour // min
    s = time % 60
    print(f'{mon} мес {d} ден {h} час {m} мин {s} сек')
else:
    y = time // year
    mon = time % year // month
    d = time % year % month // day
    h = time % year % month % day // hour
    m = time % year % month % day % hour // min
    s = time % 60
    print(f'{y} год {mon} мес {d} ден {h} час {m} мин {s} сек')
