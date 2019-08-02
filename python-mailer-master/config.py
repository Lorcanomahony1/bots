"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME = '/tmp/pymailer.log'
CSV_RETRY_FILENAME = '/tmp/pymailer.csv'
STATS_FILE = '/tmp/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# smtp settings
SMTP_HOST = 'localhost'
SMTP_PORT = '25'

# the address and name the email comes from
FROM_NAME = 'Lorcan O Mahony'
FROM_EMAIL = 'lorcanfrederickomahony@gmail.com'

# test recipients list
TEST_RECIPIENTS = [
    {'name': 'lorcan', 'email': 'lorcy7901lorka@gmail.com'},
]
