from threading import Thread, Semaphore

class AlternatePrinting:
    def __init__(self):
        self.foo_sem = Semaphore(1)
        self.bar_sem = Semaphore(0)

    def foo(self):
        print("foo")

    def bar(self):
        print("bar")

    def exec_foo(self):
        for _ in range(10):
            self.foo_sem.acquire()
            self.foo()
            self.bar_sem.release()

    def exec_bar(self):
        for _ in range(10):
            self.bar_sem.acquire()
            self.bar()
            self.foo_sem.release()

if __name__ == "__main__":
    ap = AlternatePrinting()
    t1 = Thread(target=ap.exec_bar)
    t2 = Thread(target=ap.exec_foo)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join() 