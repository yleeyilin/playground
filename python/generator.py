from typing import Generator

pth = '/Users/leeyilin/playground/python/temp.txt'

def testing_generator() -> Generator[str, None, str]:
    with open(pth, 'r') as file:
        for ln in file:
            yield ln
    return "This is the end of the generator"

def main():
    tg = testing_generator()
    while True:
        try:
            ln = next(tg)
            print(ln, end='')
        except StopIteration as e:
            print(f"Final line: {e.value}")
            break

main()
