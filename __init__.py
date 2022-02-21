from mycroft import MycroftSkill, intent_file_handler
from subprocess import call

class PiPowerOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.power.pi.intent')
    def handle_off_power_pi(self, message):
        self.speak_dialog('off.power.pi')
        call('sudo /sbin/shutdown && bash ~/mycroft-core/stop-mycroft.sh', shell=True)

    @intent_file_handler('reboot.power.pi.intent')
    def handle_reboot_power_pi(self, message):
        self.speak_dialog('reboot.power.pi')
        call('sudo /sbin/reboot', shell=True)

    @intent_file_handler('reset.power.pi.intent')
    def handle_reset_dialog(self, message):
        self.speak_dialog('reset.power.pi')
        call('bash /home/tengh/mycroft-core/start-mycroft.sh all restart', shell=True)



def create_skill():
    return PiPowerOff()

