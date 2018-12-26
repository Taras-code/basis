import multiprocessing
from time import ctime, sleep


def consumer(input_q):
    print('Into consumer:', ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of q')
    print('out of consumer:', ctime())


def producer(sequence, output_q):
    print('Into procuder:', ctime())
    for item in sequence:
        output_q.put(item)
        print('put', item, 'into q')
    print('out of producer:', ctime())


if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_q = multiprocessing.Process(target=consumer, args=(q,))
    cons_q.daemon = True
    cons_q.start()
    # sleep(1)
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.put(None)
    q.join()
