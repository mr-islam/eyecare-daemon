import subprocess as s
import time

eyeuse_title = 'Your eyes'
eyeuse_message = 'Take a break. Just 20 seconds.'

def eyeuse():
    time.sleep(1200)
    s.call(['notify-send', eyeuse_title, eyeuse_message, '--urgency=critical'])
    eyecare()

eyecare_title = 
eyecare_message = 

def eyecare():
    time.sleep(22)
    s.call(['notify-send', 'Good Job', 'You can get back to work.'])
    eyeuse()

eyeuse()
