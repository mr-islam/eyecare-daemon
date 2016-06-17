import subprocess as s
import time

eyeuse_title = 'Your eyes'
eyeuse_message = 'Take a break. Just 20 seconds.'

eyecare_title = 'Good job'
eyecare_message = 'You can get back to work.'

def eyeuse():
    time.sleep(1200)
    s.call(['notify-send', eyeuse_title, eyeuse_message, '--urgency=critical'])
    eyecare()

def eyecare():
    time.sleep(22)
    s.call(['notify-send', eyecare_title, eyecare_message])
    eyeuse()

eyeuse()

