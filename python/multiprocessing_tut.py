import multiprocessing

# note to self: this provides a trully parallel program because each processes has its own instance of GI, thus, 
# no mutex from GIL 

def func1():
    print("hello")
    input("some i.o pausing: ")
    print("meh")

def func2():
    print("world")


p1 = multiprocessing.Process(target=func1)
p2 = multiprocessing.Process(target=func2)

p1.start()
p2.start()

p1.join()
p2.join()