import time 
import asyncio
def function1():
    time.sleep(4)
    print("After 4 seconds")
def function2():
    time.sleep(4)
    print("After 4 seconds")
def function3():
    time.sleep(4)
    print("After 4 seconds")


function1()
function2()
function3()

# with out async funtion it will execute each function after four seconds

# Asynchronus Multiplication


async def functiona1(): 
    await asyncio.sleep(4)
    print("After 4 seconds")

async def functiona2():
    await asyncio.sleep(4)
    print("After 4 seconds")

async def functiona3():
    await asyncio.sleep(4)
    print("After 4 seconds")

async def main():
    l = await asyncio.gather(
        functiona1(),
        functiona2(),
        functiona3(),
    )
    print(l)  # gather() returns a list, but since functions return None, it will print [None, None, None]

asyncio.run(main())
# the above particular code will execute all function at the same instance
