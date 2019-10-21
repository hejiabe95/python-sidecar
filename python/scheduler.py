from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from algorithm import algorithm_start

jobstores = {
    'default': MemoryJobStore()
    }
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(10)
    }

job_defaults = {
    'coalesce': False,
    'max_instances': 3
    }

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(algorithm_start,args=['job_interval', ], id='job_interval',
                  trigger='interval', seconds=5,replace_existing=True)

