def echo_gen():
    while True:
        received = yield 50 # pause here and wait for a value
        print(f"Received: {received}")

g = echo_gen()
next(g)  # Prime the generator to reach the first yield
print(g.send("Hello"))  # prints "Received: Hello"
print(g.send(42))      # prints "Received: 42"


# note: observe the yield 50 tells us the gen wil return 50 when we send something, it will return this
# but what we send is passed to received 