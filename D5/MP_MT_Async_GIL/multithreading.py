import threading
import time
'''
Simple multithreaded program to calculate sum of square of numbers. 
'''


def sum_square_num(number, x="No thread"):
    res = 0 
    for num in number:
        print(f"From \t {x} : {num*num}")
        # time.sleep(0.1)
        res += num*num
        
    print(f"From \t {x} : SUM is ============> \t {res}")
    

def main():
    numbers1 = [*range(1,10,1)]
    numbers2 = [*range(10,200,10)]
    
    start = time.time()
    sum_square_num(numbers1, "No thread1")
    sum_square_num(numbers2, "No thread2")
    end = time.time()
    
    time1 = end- start 
    
    t1 = threading.Thread(target=sum_square_num, args=(numbers1,"thread1"))
    t2 = threading.Thread(target=sum_square_num, args=(numbers2,"thread2"))
    
    start = time.time()
    t1.start()
    t2.start()
    
    
    t1.join()
    t2.join()
    end = time.time()
    
    print(f"Without multithreading execution time is {time1} \n")

    print(f"With multithreading execution time is {end - start} \n")
    

if __name__ == '__main__':
    # try:
    #     main()
    # except Exception as e:
    #     print(f"An error has occured ==> \t  {e}. \n Please try again")
    main()