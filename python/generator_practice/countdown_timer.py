# Create a generator that starts from a given number \(n\) and yields numbers down to 0.

def countdown(n):
    while n >= 0:
        yield n 
        n -= 1 


if __name__ == "__main__":
    n = 10 
    gen = countdown(n)
    
    for _ in range(n + 1):
        print(next(gen))