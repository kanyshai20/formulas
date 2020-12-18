from mycroft import MycroftSkill, intent_file_handler, util
from .data import events
class Mathformula (MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('formula.intent')
    def handle_formula(self, message):
        self.speak_dialog("formula")
    
self.log.info("asking about the formula of {}")
key = "what is the formula for" + term
def create_skill()
    return Mathformula()