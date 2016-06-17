import subprocess as s
import time

command = 'notify-send'

warning_title = 'Your eyes'
warning_message = 'Take a break. Just 20 seconds.'

def warning():
    time.sleep(1200)
    s.call([command, warning_title, warning_message, '--urgency=critical']) #critical because eyes are important. And also for the different color
    success()

success_title = 'Good job'
success_message = 'You can get back to work.'

def success():
    time.sleep(22) #22 instead of 20 just to be sure
    s.call([command, success_title, success_message])
    warning()

warning()

