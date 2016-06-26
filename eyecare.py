import subprocess as s      # to pass system commands
import time                 # for pausing the script
import platform as p        # to detect linux or osx
from enums import Urgency   # urgency variables


# timer settings in seconds
work_time = 1200 
relax_time = 20
notification_expire_time_ms = 5000  # linux only

# message settings
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time)
warning_urgency = Urgency.high.value # linux only. can be either low, medium or high

success_title = 'Good job'
success_message = 'You can get back to work.'
success_urgency = Urgency.low.value  # linux only. can be either low, medium or high


# get the system platform
os = p.system().lower()


if os == 'linux':
    command = 'notify-send'  # system command being used
    expiration = '--expire-time={}'.format(notification_expire_time_ms)

    while True:
        time.sleep(work_time)
        s.call([command, warning_urgency.value, expiration, warning_title, warning_message])
        time.sleep(relax_time)
        s.call([command, success_urgency.value, expiration, success_title, success_message])
