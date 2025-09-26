import threading

# note: we often use multithreading for i/o bound processes

def func1():
    print("hello")
    input("some i.o pausing: ")
    print("meh")

def func2():
    print("world")


thrd_1 = threading.Thread(target=func1)
thrd_2 = threading.Thread(target=func2)

thrd_1.start()
thrd_2.start()

thrd_1.join()
thrd_2.join()