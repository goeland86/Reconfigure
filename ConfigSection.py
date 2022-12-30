
class ConfigSection:

    section_name: str
    settings: dict

    def __init__(self, name):
        self.section_name = name
        self.settings = dict()

    def add_setting(self, key, value):
        self.settings[key] = value

    def get_output(self):
        output = "[" + self.section_name + "]\n"
        for key in self.settings.keys():
            output += str(key) + ': ' + str(self.settings.get(key)) + "\n"
        return output

    def get_name(self):
        return self.section_name

    def get(self, key):
        return self.settings.get(key)