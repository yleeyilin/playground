# Write a generator that reads a text file line by line, but yields only lines that contain more than 3 words.

fp = "/Users/leeyilin/playground/python/temp.txt"

def file_generator(fp):
    with open(fp, 'r') as file:
        ln = file.readline()
        while ln:
            words = ln.split(" ")
            count = 0 
            res = ""
            for word in words:
                res += (word)
                res += (" ")
                count += 1 

                if count == 3:
                    yield res 
                    res = ""
                    count = 0
                
            if count > 0:
                yield res 
        
            ln = file.readline()

if __name__ == "__main__":
    gen = file_generator(fp)

    try:
        while True:
            print(next(gen))
    except StopIteration:
        pass 
