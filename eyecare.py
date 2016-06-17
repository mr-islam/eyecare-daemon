import subprocess as s
import time

#system command being used
command = 'notify-send'

#feel free to change to something more persuasive and personal
warning_title = 'Your eyes'
warning_message = 'Take a break. Just 20 seconds.'

#notify-send importance parameters. system default is 2.
priority1 = '-u low'
priority2 = '-u normal'
priority3 = '-u critical'

def warning():
    time.sleep(1200) #time in seconds
    s.call([command, warning_title, warning_message, priority3]) #critical because eyes are important. And also for the different color
    success()

#change to your liking
success_title = 'Good job'
success_message = 'You can get back to work.'

def success():
    time.sleep(22) #22 instead of 20 just to be sure
    s.call([command, success_title, success_message, priority2])
    warning()

warning()

#TODO: osx support
