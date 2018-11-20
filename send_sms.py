from twilio.rest import Client
from configs import sched_configs


class SendSMS(object):
    def __init__(self, connection=None):
        self.auth_id = sched_configs.get('sms_config', 'auth_id')
        self.token = sched_configs.get('sms_config','token')
        self.from_ = sched_configs.get('sms_config','sender')
        self.to = sched_configs.get('sms_config','receiver')
        self.client = connection

    def get_or_set_connection(self):
        """get or set connection"""
        if not self.client:
            self.client = Client(self.auth_id, self.token)
        return self.client

    def push(self, body=None):
        """ send message """
        if not self.client:
            self.get_or_set_connection()

        if not body:
            body = sched_configs.get('sms_config','default_body')
        msg = self.client.messages.create(to=self.to, from_=self.from_, body=body)
        return msg


def send_sms_api():
    """ send sms api """
    sms = SendSMS()
    sms.push()
