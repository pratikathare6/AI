# asyncio - means while waiting to execute the current task execute the other tasks concurrently
# here while sleep 1 sec its executing the other functions concurrently
# 1. async
# 2. await
# 3. gather
# 4. run

# 1. async
# function that we want to make async 
# ex - async def function1()

# 2. await 
# used to tell the pyhton that wait for this line to execute
# ex wait time.sleep(1)

# 3 gather
# run the functions concurrently
 
#  async def main():
#  await asyncio.gather(
     
#      f1()
#      f2()
#  )

# 4. run the gathered functions 

# asyncio.run(main())

import time
import asyncio

# without asyncio 

def function1():
    time.sleep(1)
    print('Function 1 done')


def function2():
    time.sleep(1)
    print('Function 2 done')



def function3():
    time.sleep(1)
    print('Function 3 done')


def main():
    function1()
    function2()
    function3()

main()

print("#"*20)

# with asyncio

async def func1():
    await asyncio.sleep(1)
    print('func 1 done')
    return '1'

async def func2():
    await asyncio.sleep(1)
    print('func 2 done')
    return '2'

async def func3():
    await asyncio.sleep(1)
    print('func 3 done')
    return '3'


async def main():
    await asyncio.gather(

          func1(),
          func2(),
          func3()
    )

asyncio.run(main())