from contextlib import contextmanager
from datetime import datetime



def func(num):
    lst = [i for i in range(20000000)]
    low = 0
    high = len(lst) - 1
    count = 0
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        ges = lst[mid]
        if ges == num:
            return f'\nчисло {ges} было найдено за {count} шага(ов).\n'
        elif ges < num:
            low = mid + 1
        elif ges > num:
            high = mid - 1



@contextmanager
def timer(foo):
    try:
        start = datetime.now()
        print(f'начало работы: {start}')
        yield  foo
    except Exception as e:
        return f'error ==> {e}'
    finally:
        end = datetime.now()
        print(f'конец работы: {end}')
        print(f'всего времени прошло: {end - start}')



if __name__ == '__main__':
    number = int(input('введите число от 1 до 20 000 000, а я попробую найти его как можно быстрее: '))

    with timer(func) as f:
        print(f(number))
    