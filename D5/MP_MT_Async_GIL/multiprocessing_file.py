import multiprocessing
import time
'''
Simple multithreaded program to calculate sum of square of numbers. 
'''


def sum_square_num(number):
    res = 0 
    for num in number:
        print(num*num)
        res += num*num
    print(f"SUM is ============> \t {res}")
    

def main():
    numbers1 = [*range(1,100000)]
    numbers2 = [*range(10,200000)]
    
    start = time.time()
    sum_square_num(numbers1)
    sum_square_num(numbers2)
    end = time.time()
    
    time1 = end- start 
    
    p1 = multiprocessing.Process(target=sum_square_num, args=(numbers1,))
    p2 = multiprocessing.Process(target=sum_square_num, args=(numbers2,))
    
    start = time.time()
    p1.start()
    p2.start()
    end = time.time()
    time2 = end - start
    
    print(f"PRocess of process is {p1.pid}")
    print(f"PRocess of process is {p2.pid}")
    
    p1.join()
    p2.join()
    
    print(f"Without multiprocessing execution time is {time1} \n")

    print(f"With multiprocessing execution time is {time2} \n")
    

if __name__ == '__main__':
    # try:
    #     main()
    # except Exception as e:
    #     print(f"An error has occured ==> \t  {e}. \n Please try again")
    main()