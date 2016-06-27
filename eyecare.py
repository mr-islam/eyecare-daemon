import subprocess as s      # to pass system commands
import time                 # for pausing the script
import platform as p        # to detect linux or osx
import os
from enums import Urgency   # config


# timer settings
work_time = 4
relax_time = 2
notification_expire_time_ms = 5000  # linux only

# message settings
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time)
warning_urgency = Urgency.high  # linux only. can be either low, medium or high

success_title = 'Good job'
success_message = 'You can get back to work.'
success_urgency = Urgency.low   # linux only. can be either low, medium or high


# get the system platform
os1 = p.system().lower()

# 1 is preferred, but try 2 if you encounter an `OSError`
command_method = 1


if os1 == 'linux':
    command = 'notify-send'  # command being used
    expiration = '--expire-time={}'.format(notification_expire_time_ms)

    while command_method == 1:
        time.sleep(work_time)
        s.call([command, warning_urgency, expiration, warning_title, warning_message])
        time.sleep(relax_time)
        s.call([command, success_urgency, expiration, success_title, success_message])

    while command_method == 2:
        warning_cmd = "{0} {1} {2} \"{3}\" \"{4}\"".format(command,warning_urgency,expiration,warning_title,warning_message)
        success_cmd = "{0} {1} {2} \"{3}\" \"{4}\"".format(command,success_urgency,expiration,success_title,success_message)

        time.sleep(work_time)
        os.system(warning_cmd)
        time.sleep(relax_time)
        os.system(success_cmd)

if os1 == 'darwin':  # thats OSX
    command1 = 'osascript -e'
    command2 = 'display notification'  # osx command, extra ' has to be there!
    with_title = 'with title'
    warning_cmd = "{0} \'{1} \"{2}\" {3} \"{4}\"\'".format(command1,command2,warning_message,with_title,warning_title)
    success_cmd = "{0} \'{1} \"{2}\" {3} \"{4}\"\'".format(command1,command2,success_message,with_title,success_title)

    while True: #TODO: implement command_method 1 and 2
        time.sleep(work_time)
        os.system(warning_cmd)
        time.sleep(relax_time)
        os.system(success_cmd)

#TODO: add customizability for osx command (http://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel/115373#115373)
#TODO: option between subprocess and os
#TODO: detect python version, use either `os.system` or `subprocess.call` (http://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script)
