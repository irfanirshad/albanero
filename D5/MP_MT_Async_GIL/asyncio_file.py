import asyncio
import time
'''
Simple multithreaded program to calculate sum of square of numbers. 
'''

# keep in mind that , asyncio is slower than normal multithreaded
async def sum_square_num(number):
    res = 0 
    for num in number:
        print(f"The number is \t {num} \t {num*num}")
        res += num*num
        await asyncio.sleep(0.1)
    print(f"SUM is ============> \t {res}")
    

def main():
    numbers1 = [*range(1,50)]
    numbers2 = [*range(50,100)]
    
    start = time.time()
    #
    sum_square_num(numbers1)
    sum_square_num(numbers2)
    end = time.time()
    
    time1 = end- start 
    print(f"Without ASYNCIO execution time is {time1} \n")
    
    
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