from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler

#importing the callmsg function from script.py that you have made
from script import callmsg

ist = pytz.timezone('Asia/Kolkata')

sched = BlockingScheduler()

# Schedule the python script to be called everyday from monday to friday at 7:17 P.M. You change the time as per your need.
sched.add_job(callmsg, 'cron', day_of_week='mon-fri', hour=19, minute=17, timezone=ist)

sched.start()
