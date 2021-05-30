from adapt.intent import IntentBuilder
from chatterbox import ChatterboxSkill, intent_handler

class CookingSkill(ChatterboxSkill):
    
    def __init__(self):
        super().__init__()
        self.started_cooking = False

    def initialize(self):
        my_setting = self.settings.get('my_setting')


    @intent_handler('start.cooking.intent')
    def handle_start_cooking_intent(self, message):
        self.speak_dialog("start.cooking")
        self.started_cooking = True

    def stop(self):
        self.speak_dialog("stop.cooking")
        self.started_cooking = False

def create_skill():
    return CookingSkill()