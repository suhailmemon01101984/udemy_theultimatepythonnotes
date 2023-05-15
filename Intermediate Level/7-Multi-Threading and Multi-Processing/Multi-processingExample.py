import multiprocessing
import time

# A function to print a message and sleep for a given number of seconds
def print_message(message, sleep_time):
    time.sleep(sleep_time)
    print(message)

if __name__ == '__main__':
    # Create a new process to print the first message
    p1 = multiprocessing.Process(target=print_message, args=('Hello', 2))

    # Create a new process to print the second message
    p2 = multiprocessing.Process(target=print_message, args=('World', 1))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()


'''
In this example, we use the multiprocessing module to create two new processes that will run simultaneously.
 We define a function print_message that takes a message and a sleep time as input, sleeps for the given number of seconds, 
 and then prints the message. We then create two new processes p1 and p2 that will call print_message with different arguments.
We start both processes with the start method, and then wait for both processes to finish using the join method. 
This ensures that both processes have finished before the program exits.
'''

