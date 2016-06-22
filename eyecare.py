import subprocess as s  # to pass system commands
import time  # for pausing the script
import platform as p  # to detect linux or osx

os = p.system()

# timer settings
work_time_ms = 1200
relax_time_ms = 22
# feel free to change to something more persuasive and personal
warning_title = 'Your eyes'
warning_message = 'Take a break. Just {} seconds.'.format(relax_time_ms)
success_title = 'Good job'
success_message = 'You can get back to work.'

# to specify custom timeout, use `--expire-time=TIME` flag after priority. (TIME in milliseconds)

while os.lower() == 'linux':
    command = 'notify-send'  # command being used

    # notify-send importance parameters. system default is 2.
    priority1 = '--urgency=low'
    priority2 = '--urgency=normal'
    priority3 = '--urgency=critical'

    # the actual script
    time.sleep(work_time_ms)
    s.call([command, priority3, warning_title, warning_message])
    time.sleep(relax_time_ms)
    s.call([command, priority2, success_title, success_message])

while os.lower() == 'darwin':  # thats OSX
    command1 = 'osascript -e'
    command2 = 'display notification'  # osx command, extra ' has to be there!
    success_title = 'Good job'
    warning_title = 'Your eyes'  # againg, trailing ' is needed!

    time.sleep(work_time_ms)
    s.call([command1, warning_message, 'with title', warning_title])
    time.sleep(relax_time_ms)
    s.call([command1, success_message, 'with title', success_title])
