def decorator(func):
    def wrapper():
        print("HERE1")
        func()
        print("HERE2")
    
    return wrapper

@decorator
def myworld():
    print("Hello World")

if __name__ == "__main__":
    myworld()