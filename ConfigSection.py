
class ConfigSection:

    section_name: str
    settings: dict

    def __init__(self, name):
        self.section_name = name
        self.settings = dict()

    def add_setting(self, key, value):
        self.settings.update(key, value)

    def get_output(self):
        output = ""
        output += "[" + self.section_name + "]\n"
        for key in self.settings.keys():
            output += key + ": " + str(self.settings.get(key)) + "\n"
