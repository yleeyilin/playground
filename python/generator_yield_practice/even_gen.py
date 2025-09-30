def generator(input_lst):
    fptr = 0
    while fptr < len(input_lst):  # stop at end of list
        if input_lst[fptr] % 2 == 0:  # yield only evens
            yield input_lst[fptr]
        fptr += 1
    # fptr = 0 
    # while True:
    #     while fptr < len(input_lst) and input_lst[fptr] % 2 != 0:
    #         fptr += 1 
        
    #     yield input_lst[fptr]
    #     fptr += 1 

if __name__ == "__main__":
    test_lst = [1,2,3,4,5,6,6,8,9,9,10]
    gen = generator(test_lst)

    for i in range(5):
        print(next(gen))