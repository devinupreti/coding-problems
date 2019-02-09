# PROBLEM :  Implement a job scheduler
#            which takes in a function f and an integer n,
#            and calls f after n milliseconds.

# Source : Apple, DCP

import time

def job():
    print("Job completed")
    
def scheduler(func, millisec):
    sec = millisec * 0.001
    time.sleep(sec)
    func()
    return

scheduler(job, 10000) # 10 seconds
