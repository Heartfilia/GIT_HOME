from contextlib import contextmanager


class MyResource:
    # def __enter__(self):
    #     print('enter it')
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('exit it')

    def go(self):
        print('yes it is')


@contextmanager
def test():
    print('enter it')
    yield MyResource()
    print('exit it')


# with test() as t:
#     t.go()


@contextmanager
def book_mark():
    print('<', end='')
    yield
    print('>')


with book_mark():
    print('加个书名号', end='')
