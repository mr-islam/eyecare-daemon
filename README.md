# eyecare-daemon

![Alt text](https://i.imgur.com/B5HF85r.png "Demonstration")

Save your eyes by following the [20/20/20](http://www.labnol.org/software/computer-eye-exercise/14069/) rule! `eyecare-daemon` will send you a notification every 20 minutes, urging you to protect your eyes by looking 20 feet away for 20 seconds. Once your eyes have recovered from their toil, the daemon will let you know that you can get back to work. <sup>Such an essential for health script should be included by default in all distros. </sup>

____

## Installation

Simplicity itself.

Download both `eyecare.py` and `enums.py` and place them in the same folder. Set the following code to run at startup (eg. putting it in `xinit.rc` or your distro settings):

    python ~/path/to/file/eyecare.py

## Details

| Setting  | Detail        |
|----------|---------------|
| `work_time` |  Default `1200`, in seconds |
| `relax_time` | Default `20`, in seconds |
| `notification_expire` - Linux only | Default `5000`, in ms |
| `command_method` | `modern` is preferred, but try `legacy` if you encounter an `OSError`-- this error happens when your shell python path variable is not set, so please do set it. `legacy` is also the default for osx as most people (I presume) do not have the path variable set, and those who do will comment out this default anyway :) |

## Dependencies

* python
* `libnotify` for linux notification

## Notes
Confirmed to work on:
* Ubuntu 16.04 LTS (meaning derivative distros also should work)
* Arch Linux with `libnotify-bin`, and something to handle notifications installed (`dunst` is used in the screenshot)

____

## Hall of Fame

* [@ragerin](https://github.com/ragerin) for a very helpful fork which was merged a long while ago, which is the foundation of today's daemon
* [/u/guiltydoggy](https://www.reddit.com/user/guiltydoggy) for testing the osx script repeatedly, and putting up with my relentless revisions
