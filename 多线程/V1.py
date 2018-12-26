import time
import _thread as thread


def loop1(in1):
    print('Start loop1 at:', time.ctime())
    print('我是参数', in1)
    time.sleep(4)
    print('End loop1 at:', time.ctime())


def loop2(in1, in2):
    print('Start loop2 at:', time.ctime())
    print('我是参数', in1, '和参数', in2)
    time.sleep(2)
    print('End loop2 at:', time.ctime())


def main():
    print('Starting at:', time.ctime())
    t1 = thread.start_new_thread(loop1, ('张三',))
    t2 = thread.start_new_thread(loop2, ('李四', '王二'))
    print('All done at:', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)


