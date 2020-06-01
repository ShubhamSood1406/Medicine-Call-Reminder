from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from script import msg

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(msg, 'interval', seconds = 60)

sched.start()