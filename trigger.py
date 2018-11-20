
from datetime import datetime

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BlockingScheduler, BackgroundScheduler
from pytz import utc


class Trigger(object):
    def __init__(self):
        self.job_store = {'jobstore_alias':MemoryJobStore()}
        self.timezone = utc

    def configure(self):
        self.scheduler = BackgroundScheduler(
            jobstores=self.job_store,
            timezone=self.timezone
        )

    def add(self, func):
        self.scheduler.add_job(func, self.trigger_type, next_run_time=self.runtime)

    def modify(self):
        #self.trigger.modify()
        pass

    def show(self):
        #self.trigger.show()
        pass

    def start(self):
        self.scheduler.start()


class OneTimeTrigger(Trigger):

    def __init__(self):
        self.runtime = datetime.utcnow()
        self.trigger_type = 'date'
        super(self.__class__, self).__init__()


class IntervalTrigger(Trigger):
    def __init__(self):
        # runtime calcualtion
        self.runtime = 0 #TODO
        self.trigger_type = 'interval'
        super(self.__class__, self).__init__()


class PeriodicTrigger(Trigger):
    def __init__(self):
        self.runtime = 0 # TODO
        self.trigger_type = 'cron'
        super(self.__class__, self).__init__()
