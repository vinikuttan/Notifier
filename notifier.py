
import time
from logger import error_log, info_log, initialize_logger
from trigger import OneTimeTrigger, IntervalTrigger, PeriodicTrigger
from sms_exceptions import BadArgumentError
from send_sms import send_sms_api

payload = {'type': 'onetime'}


def main():
    """ entry point """
    
    def raise_():
        msg = "input params required valid job type "
        error_log.error("invalid job type passed : {0}".format(job_type))
        raise BadArgumentError("input params required valid job type ")

    job_type = payload.get('type', 'onetime') # default value `onetime`
    error_log, info_log = initialize_logger()

    trigger = {
        'onetime': OneTimeTrigger,
        'interval': IntervalTrigger,
        'periodic': PeriodicTrigger
    }.get(job_type, raise_)

    trig = trigger()
    trig.configure()
    trig.add(send_sms_api)
    trig.start()
    info_log.info("job successfully scheduled")
    
    # to make active thread alive
    time.sleep(100)


if __name__=="__main__":
    main()
