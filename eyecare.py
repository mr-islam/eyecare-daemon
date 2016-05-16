import subprocess as s
import time


def eyeuse():
    time.sleep(1200)
    s.call(['notify-send', 'Your Eyes', 'Take a break. Just 20 seconds.', '--urgency=critical'])
    eyecare()

def eyecare():
    time.sleep(22)
    s.call(['notify-send', 'Good Job', 'You can get back to work.'])
    eyeuse()

eyeuse()
