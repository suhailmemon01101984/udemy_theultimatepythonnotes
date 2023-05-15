import threading
import time

# A function to print a message and sleep for a given number of seconds
def print_message(message, sleep_time):
    time.sleep(sleep_time)
    print(message)

# Create a new thread to print the first message
t1 = threading.Thread(target=print_message, args=('Hello', 2))

# Create a new thread to print the second message
t2 = threading.Thread(target=print_message, args=('World', 1))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()


'''
In this example, we use the threading module to create two new threads that 
will run simultaneously. We define a function print_message that takes a 
message and a sleep time as input, sleeps for the given number of seconds, 
and then prints the message. We then create two new threads t1 and t2 that will 
call print_message with different arguments. We start both threads with the start 
method, and then wait for both threads to finish using the join method. 
This ensures that both threads have finished before the program exits.
'''