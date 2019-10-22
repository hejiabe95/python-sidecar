from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from algorithm import algorithm_start
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ADDED

def once_listener(ev):
    if ev.code == EVENT_JOB_ADDED:
        if ev.job_id == 'job_once':
            scheduler.get_job(job_id='job_interval').pause()
    if ev.code == EVENT_JOB_EXECUTED:
        if ev.job_id == 'job_once':
            scheduler.get_job(job_id='job_interval').resume()

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
                  trigger='interval', seconds=3,replace_existing=True)
scheduler.add_listener(once_listener, EVENT_JOB_ADDED|EVENT_JOB_EXECUTED)

