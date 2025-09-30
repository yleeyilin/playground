def recv_smth():
    smth = ""
    while True:
        smth = yield smth
        print(f"Recevied the following payload: {smth}")

if __name__ == "__main__":
    gen = recv_smth()
    next(gen)
    payloads = [1,2,3,4,5]
    for p in payloads:
        print(f"prev one was {gen.send(p)}")