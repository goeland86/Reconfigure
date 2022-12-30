import tkinter as tk
from Printer import PrinterConfig
from Board import BoardConfig
from Stepper import StepperConfig
import ConfigSection


class Reconfigure:
    border_effects = {"flat": tk.FLAT, "sunken": tk.SUNKEN, "raised": tk.RAISED, "groove": tk.GROOVE,
                      "ridge": tk.RIDGE}

    config: [ConfigSection]

    def __init__(self):
        self.mainframe = None
        self.window = None
        self.board_config = BoardConfig(self)
        self.printer_config = PrinterConfig(self)
        self.stepper_config = StepperConfig(self)
        self.config = list()

    def create_window(self):
        self.window = tk.Tk()
        self.mainframe = tk.Frame(master=self.window, relief=self.border_effects.get("raised"))
        self.mainframe.pack()

    def destroy_window(self):
        self.mainframe.destroy()
        self.window.destroy()

    def add_config_section(self, config_section):
        # print("adding section " + config_section.get_name())
        self.config.append(config_section)


main = Reconfigure()
main.board_config.board_selection_gui(main)

print("Config generated: ")
for section in main.config:
    print(section.get_output())
    print("\n\n")
# main.window.quit()
