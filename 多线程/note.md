http://www.babeaz.com/python/UnderstandingGIL.pdf
#多线程 vs多进程
- 程序： 一堆代码以文本形式存入一个文档
- 进程： 程序运行的一个状态
    - 包含地址，内存，数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以由多个线程
    - 轻量级的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL)
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能够有一个控制线程在执行
- Python包
    - thread：有问题，不好用，python3改成了_thread
    - threading: 通行的包
    - 顺序执行，耗时比较长；改进多线程，缩短总时间，使用_thread;多线程，传参数（thread.start_new_thread(main,(in1,in2))
    - 不需要守护线程，随主线程结束而结束
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xxx, args(xxx,))
        2. t.start() 启动线程
        3. t.join() 等待多线程执行完毕
        4. 守护线程-daemon
            - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境有关（t.setdaemon（））
            - 主函数运行完后，线程还会继续跑（需要守护线程），模块运行完后，线程不会跑了
        -线程常用属性
            - threading.currentThread: 返回当前线程变量
            - 。。。
    - 直接继承自threading.Thread
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
        - V3
        - demo1 工业方案例
- 共享变量
    -  共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题
    - 解决变量：锁，信号灯
    - 锁（Lock）：
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法（lock=threading.Lock（）;lock.acquire();lock.release（））
            - 上锁
            - 使用共享，放心使用
            - 取消锁， 释放锁  
        - 锁谁：哪个资源需要多线程共享，锁哪个
        - 理解锁：锁其实不是锁住谁，而是一个令牌 
    - 线程安全问题： 
        - 如果一个资源/变量，它对于多线程来讲，不用加锁也不会引起任何问题，则称为线程安全
        - 线程不安全变量类型：list，set，dict
        - 线程安全变量类型： queue（队列）
    - 生产者消费者问题
        - 一个模型，可以用来搭建消息队列
        - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队可以理解为一个特殊的list
    - 死锁问题
    - 锁的等待时间问题（lock.acquire(timeout=5))
    - semphore（ps：semphore=threading.Semphore(3)；semphore.acquire()）
        - 允许一个资源最多由几个多线程同时使用
    - threading.Timer（threading.Timer（6，main函数名））
        -Timer是利用多线程，在指定时间后启动一个功能  
    - 可重入锁（threading.RLcok() ）
        - 一个锁，可以被一个线程多次申请
        - 主要解决递归调用的时候，需要重新申请锁的情况  
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是python进程的主要替代方案
    - python2.3后引入
- multiprocessing（p = multiprocessing.Process(target = 函数名，args = (5,))）
    - 使用threading借口派生，使用子进程 
    - 允许为多核或者多cpu派生进程，接口跟threading非常相似
    - python2.6
    
-concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2后引入
# 多进程
- 进程间通讯（InterprocessCommunication,IPC）
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象
    - 派生子类
- 在os中查看pid（进程id），ppid（父进程id）以及他们的关系
- 生产者消费者模型
    - JoinableQueue (带参数函数如果没有参数，不会执行)PS：V
    - 队列里哨兵的使用， 案例V6(由几个子线程就在队列里放几个元素q.put(None))
    
            