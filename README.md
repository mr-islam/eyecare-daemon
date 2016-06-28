# eyecare-daemon

![Alt text](https://i.imgur.com/B5HF85r.png "Demonstration")

For the system notification, it uses the linux `notify-send` command, and should work with any distro (tested on Arch using Dunst for notifications). Set it to run on startup, and save your eyes!

Now, you can easily change the messages, and also the system command used. Even more fresh: experimental OSX support is here!
____

# Installation

Simplicity itself.

Download both `eyecare.py` and `enums.py` and place them in the same folder. Set the following code to run at startup (eg. putting it in `xinit.rc` or your window manager config file):

    python ~/path/to/file/eyecare.py

# Dependencies

* python
* `libnotify` for linux notification (sometimes packaged as `libnotify-bin`)
* ___ for Windows [coming soon!]

____

# Hall of Fame

* @ragerin for a very helpful fork which was merged a long while ago
* /u/guiltydoggy for testing the osx script and putting up with my relentless revisions

