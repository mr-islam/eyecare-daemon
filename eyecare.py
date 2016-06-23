import subprocess as s  #to pass system commands
import time as t        #for the timer
import platform as p    #to detect linux or osx

#feel free to change to something more persuasive and personal
warning_title =     "Your eyes"
warning_message =   "Take a break. Just 20 seconds."
success_title =     "Good job"
success_message =   "You can get back to work."

#timer_settings
screen_time =   '1200'
rest_time =     '22'

os = p.system()

while os == 'Linux':
    command = 'notify-send' #system command

    #notify-send parameters
    priority1 =     '--urgency=low'
    priority2 =     '--urgency=normal'      #system default
    priority3 =     '--urgency=critical'
    timeout =       '--expire-time=22'

    #the actual script
    t.sleep(screen_time)
    s.call([command, priority3, timeout, warning_title, warning_message])
    t.sleep(rest_time)
    s.call([command, priority2, timeout, success_title, success_message])

while os == 'Darwin': #thats OSX
    command1 =      "osascript -e"
    command2 =      "'display notification" #osx command, extra ' has to be there!
    success_title = "Good job'" 
    warning_title = "Your eyes'" #again, trailing ' is needed!

    time.sleep(4) #short timer to aid in testing
    s.call([command1, warning_message, 'with title', warning_title])
    time.sleep(2)
    s.call([command1, success_message, 'with title', success_title])

