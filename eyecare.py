import subprocess as s      # to pass system commands
import time                 # for pausing the script
import platform as p        # to detect linux or osx
import os
#from enums import Urgency   # config


# timer settings
work_time = 4
relax_time = 2
#notification_expire_time_ms = 5000  # linux only

# message settings
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time)
#warning_urgency = Urgency.high  # linux only. can be either low, medium or high

success_title = 'Good job'
success_message = 'You can get back to work.'
#success_urgency = Urgency.low   # linux only. can be either low, medium or high


# get the system platform
os1 = p.system().lower()


if os1 == 'linux':
    command = 'notify-send'  # command being used
    expiration = '--expire-time={}'.format(notification_expire_time_ms)

    while True:
        time.sleep(work_time)
        s.call([command, warning_urgency, expiration, warning_title, warning_message])
        time.sleep(relax_time)
        s.call([command, success_urgency, expiration, success_title, success_message])

if os1 == 'darwin':  # thats OSX
    command1 = 'osascript -e'
    command2 = 'display notification'  # osx command, extra ' has to be there!
#osascript -e 'display notification "Lorem ipsum dolor sit amet" with title "Title"'
    while True:
        time.sleep(work_time)
        os.system('\"' + command1 + ' \'' + command2 + ' \"' + warning_message + '\" ' + 'with title' + ' \"' +  warning_title + '\"' + '\'' + '\"')
        time.sleep(relax_time)
        os.system('\"' + command1 + ' \'' + command2 + ' \"' + success_message + '\" ' + 'with title' + ' \"' +  success_title + '\"' + '\'' + '\"')

#TODO: detect python version, use either `os.system` or `subprocess.call` (http://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script)
#TODO: undo linux breakage
#TODO: fix enum like reddit bro said (https://www.reddit.com/r/osx/comments/4q3aml/anyone_willing_to_help_test_this_python_script/d4py2v3)
