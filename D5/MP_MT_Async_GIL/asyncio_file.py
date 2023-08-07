import asyncio
import time
'''
Simple multithreaded program to calculate sum of square of numbers. 
'''


async def sum_square_num(number):
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
    
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(sum_square_num(numbers1,)),
        loop.create_task(sum_square_num(numbers2)), # type: ignore
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end = time.time()
    time2 = end - start
    
    
    
    print(f"Without ASYNCIO execution time is {time1} \n")

    print(f"With asynchronous processing time is {time2} \n")
    

if __name__ == '__main__':
    # try:
    #     main()
    # except Exception as e:
    #     print(f"An error has occured ==> \t  {e}. \n Please try again")
    main()