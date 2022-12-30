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

    def create_window(self):
        self.window = tk.Tk()
        self.mainframe = tk.Frame(master=self.window, width=400, height=400, relief=self.border_effects.get("raised"))
        self.mainframe.pack()

    def destroy_window(self):
        self.mainframe.destroy()
        self.window.destroy()

    def add_config_section(self, config_section):
        self.config.append(config_section)


main = Reconfigure()
main.board_config.board_selection_gui(main)

print("Board: ", main.board_config.get_board())
print("Printer: ", main.printer_config.get_printer_config())
print("Steppers: ", main.stepper_config.get_stepper_config())
print("Stepper_options: ", main.stepper_config.get_stepper_options())

# main.window.quit()
