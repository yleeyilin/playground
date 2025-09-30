def recv_smth():
    while True:
        smth = yield 
        print(f"Recevied the following payload: {smth}")

if __name__ == "__main__":
    gen = recv_smth()
    next(gen)
    payloads = [1,2,3,4,5]
    for p in payloads:
        gen.send(p)