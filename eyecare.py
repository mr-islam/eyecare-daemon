import subprocess as s #to pass system commands
import time  #for pausing the script
import platform as p #to detect linux or osx

os = p.system()

#feel free to change to something more persuasive and personal
warning_title = "Your eyes"
warning_message = "Take a break. Just 20 seconds."
success_title = "Good job"
success_message = "You can get back to work."

#to specify custom timeout, use `--expire-time=TIME` flag after priority. (TIME in milliseconds)

while os == 'Linux':
    command = 'notify-send' #command being used

    #notify-send importance parameters. system default is 2.
    priority1 = '--urgency=low'
    priority2 = '--urgency=normal'
    priority3 = '--urgency=critical'

    #the actual script
    time.sleep(1200)
    s.call([command, priority3, warning_title, warning_message])
    time.sleep(22)
    s.call([command, priority2, success_title, success_message])

while os == 'Darwin': #thats OSX
    command1 = 'osascript -e'
    command2 = "'display notification" #osx command, extra ' has to be there!
    success_title = "Good job'" 
    warning_title = "Your eyes'" #againg, trailing ' is needed!

    time.sleep(4)
    s.call([command1, warning_message, 'with title', warning_title])
    time.sleep(2)
    s.call([command1, success_message, 'with title', success_title])
