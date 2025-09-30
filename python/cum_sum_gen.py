from typing import Generator

def cum_sum() -> Generator[int, int, None]:
    total = 0

    while True:
        new_val = yield total
        total += new_val

if __name__ == "__main__":
    cs_gen = cum_sum()
    print(next(cs_gen)) # give us the total 
    while True:
        to_add = input("Value to add: ")
        total = cs_gen.send(int(to_add)) # pass it to the yield variable 
        print(f"curr sum is: {total}")
