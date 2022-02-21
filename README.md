# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/bug.svg" card_color="#F1F3F4" width="50" height="50" style="vertical-align:bottom"/> Pi Power Off
Allows mycroft to shutdown and reboot on raspberry pi, as well as restart all services if needed.

## About
I created this skill because i did not want to use picroft. instead, i used mycroft-core on raspbian 64 bit os. the shutdown skill that is currently installed does not utilize a command line call to sudo shutdown, sudo reboot, or bash mycroft-core/start-mycroft.sh all restart. utilizing this skill allows a user in my situation to restart mycroft's services, shutdown, and reboot their raspberry pi.

## Note
You may need to add mycroft ALL=(ALL) NOPASSWD: /sbin/shutdown,/sbin/reboot to your /etc/sudoers file. To do this, open a terminal and type the following:

sudo nano /etc/sudoers

When this file opens, add the following:

mycroft ALL=(ALL) NOPASSWD: /sbin/shutdown,/sbin/reboot 

below root in the # user privilege specification section

**Also, the Mycroft System or Stop skill is currently interferring with this skill. Mycroft downloads that skill everytime it updates. I am in the process of figuring out a way to either block or permanently remove the System/Stop skill so my pi-power-off-skill can work on my system.**

## Examples
* "Shutdown"
* "Goodnight"
* "Good night"
* "Power off"
* "Power down"

## Credits
Travis Engh

## Category
**Configuration**

## Tags
#shutdown
#reboot
#restartskills

