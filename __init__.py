from mycroft import MycroftSkill, intent_file_handler


class PiPowerOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.power.pi.intent')
    def handle_off_power_pi(self, message):
        self.speak_dialog('off.power.pi')


def create_skill():
    return PiPowerOff()

