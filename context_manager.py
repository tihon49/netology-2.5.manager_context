from contextlib import contextmanager
from datetime import datetime



def read_lines(path):
    count = 0
    file = open (path, encoding='Latin-1')
    lines = file.readlines()

    for line in lines:
        count += 1

    return f'в файле {count} строк(и)'



@contextmanager
def timer(foo):
    try:
        start = datetime.now ()
        yield  foo
    except Exception as e:
        return f'error ==> {e}'
    finally:
        end = datetime.now()
        print(f'время работы функции: {end - start}')



if __name__ == '__main__':
    with timer(read_lines('test.txt')) as f:
        print(f)


