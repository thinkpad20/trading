from datetime import datetime, timedelta
from threading import Timer
import time

start_time = datetime.strptime('08:30:00 09/16/2013', '%H:%M:%S %m/%d/%Y')
stop_time = datetime.strptime('16:00:00 09/16/2013', '%H:%M:%S %m/%d/%Y')


now = datetime.now()

# def time_till_start():
#     if 0 <= now.weekday() <= 3 or now.weekday() == 6:
#         # then we're at 

while 0 <= now.weekday() <= 4 and start_time <= now <= stop_time:
    print "hey"
    time.sleep(1)

# while True:
#     if start_time <= now <= stop_time:
#         print "running task"
#     else:
#         if now < start_time:
#             print "start is approaching"
#             delta = start_time - now


# def task():
#     print "call to task!"

# def wait():
#     return int(datetime.now().minute) < 27

# def run():
#     return 27 <= int(datetime.now().minute) < 28

# def do_job(wait_cond, run_cond, task, timer, wait_timer):
#     while True:
#         if wait_cond():
#             print "have to wait"
#             time.sleep(wait_timer)
#         elif run_cond():
#             print "running task"
#             task()
#             time.sleep(timer)
#         else:
#             print "loop finished"
#             break

# do_job(wait, run, task, 5, 30)