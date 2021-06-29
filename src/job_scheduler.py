"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time


def job_scheduler(f, n):
    time.sleep(n / 1000)
    f()

def hello():
    print("hello!")

##########

if __name__ == '__main__':
    start = time.time()
    print(f"Start: {start}")
    job_scheduler(hello, 1000)
    end = time.time()
    print(f"End: {end}")