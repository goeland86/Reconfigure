import tkinter as tk
from Printer import PrinterConfig
from Board import BoardConfig
from Stepper import StepperConfig
from Extruder import ExtruderConfig
import ConfigSection


class Reconfigure:
    border_effects = {"flat": tk.FLAT, "sunken": tk.SUNKEN, "raised": tk.RAISED, "groove": tk.GROOVE,
                      "ridge": tk.RIDGE}

    config: [ConfigSection]

    def __init__(self):
        self.mainframe = None
        self.window = None
        self.board_config = BoardConfig(self)
        self.pin_map = None
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

    def set_pin_map(self, pin_map):
        self.pin_map = pin_map

    def init_printer(self):
        self.printer_config = PrinterConfig(self)

    def init_stepper(self):
        self.stepper_config = StepperConfig(self)

    def init_extruder(self):
        self.extruder_config = ExtruderConfig(self)

main = Reconfigure()
main.board_config.board_selection_gui(main)

print("Config generated: ")
for section in main.config:
    print(section.get_output())
    print("\n\n")
# main.window.quit()
