from contextlib import contextmanager
from datetime import datetime
import time



def read_lines(path):
    count = 0
    file = open (path, encoding='Latin-1')
    lines = file.readlines()

    with open('out.txt', 'w') as out_file:
        for line in lines:
            line = line.strip()
            count += 1
            print(line)
            out_file.write(line + '\n')

        return f'\nв файле {count} строк(и)'



@contextmanager
def timer(foo):
    try:
        yield  foo
    except Exception as e:
        return f'error ==> {e}'



if __name__ == '__main__':
    start = datetime.now()

    with timer(read_lines('test.txt')) as f:
        print(f)
    
    end = datetime.now()

    print(f'начало работы: {start}')
    print(f'окончание работы: {end}')
    print(f'всего времени ушло: {end - start}')


