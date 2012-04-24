import requests

class Client(object):

    LAUNCHPAD_URL = 'https://launchpad.37signals.com'
    BASE_URL = 'https://basecamp.com/%s/api/v1'

    def __init__(self, access_token, user_agent, account_id=None):
        """Initialize client for making requests.

        user_agent -- string identifying the app, and an url or email related
        to the app; e.g. "BusyFlow (http://busyflow.com)".
        """
        self.account_id = account_id
        self.session = requests.session(
                headers={'User-Agent': user_agent,
                         'Authorization': 'Bearer %s' % access_token,
                         'Content-Type': 'application/json; charset=utf-8'})

    def accounts(self):
        url = '%s/authorization.json' % self.LAUNCHPAD_URL
        return self.session.get(url).content