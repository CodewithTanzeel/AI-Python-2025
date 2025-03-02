import threading
import time

# Function to simulate a CPU-intensive task
def CpuTask():
    total = 0
    for _ in range(10**7):  # A large loop to keep the CPU busy
        total += 1
    # Print the name of the thread that completed the task
    print(f"Task completed by {threading.current_thread().name}")

# Record the start time of execution
startTime = time.time()

# Creating two threads to run the CPU-intensive task
threadOne = threading.Thread(target=CpuTask, name="Thread-1")
threadTwo = threading.Thread(target=CpuTask, name="Thread-2")

# Start both threads
threadOne.start()
threadTwo.start()

# Wait for both threads to complete execution
threadOne.join()
threadTwo.join()

# Record the end time of execution
endTime = time.time()

# Print the total execution time
print(f"Total execution time: {endTime - startTime:.2f} seconds")
