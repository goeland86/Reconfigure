from typing import Dict, Any
import tkinter as tk
from ConfigSection import ConfigSection
from Recore import Recore


class PrinterConfig:

    def __init__(self, parent):
        self.board = None
        self.parent = parent
        self.printer = ConfigSection("printer")

    def create_printer_section(self, parent, board):
        self.board = board
        self.parent.create_window()
        return_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"),
                                  text="Back",
                                  width=5, height=5, bg="black", fg="white")
        return_button['command'] = self.return_to_board_selection_gui
        return_button.pack()
        # list of options taken from https://www.klipper3d.org/Config_Reference.html#printer
        geometry_options = ["cartesian", "corexy", "corexz", "hybrid_corexy", "hybrid_corexz", "rotary_delta", "delta",
                            "deltesian", "polar", "winch", "none"]
        geometry_selected = tk.StringVar(parent.mainframe)
        geometry_selected.set(geometry_options[0])
        geometry_selection = tk.OptionMenu(parent.mainframe, geometry_selected, *geometry_options)
        geometry_selection.pack()
        max_velocity = "100"
        max_velocity_label = tk.Label(master=parent.mainframe, text="Max velocity")
        max_velocity_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10,
                                      textvariable=max_velocity)
        max_velocity_entry.insert(index=0, string="100")
        max_velocity_label.pack()
        max_velocity_entry.pack()
        max_accel = "1000"
        max_accel_label = tk.Label(master=parent.mainframe, text="Max Accel")
        max_accel_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10, textvariable=max_accel)
        max_accel_entry.insert(index=0, string="1000")
        max_accel_label.pack()
        max_accel_entry.pack()
        square_corner_velocity = 5
        scv_label = tk.Label(master=parent.mainframe, text="Square Corner Velocity")
        scv_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10,
                             textvariable=square_corner_velocity)
        scv_entry.insert(0, square_corner_velocity)
        scv_label.pack()
        scv_entry.pack()
        printer_confirm_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"),
                                           text="Ok", width=5, height=5, bg="black", fg="white")
        printer_confirm_button['command'] = \
            lambda kinematics=geometry_selected, max_v=max_velocity, max_a=max_accel, \
                   scv=scv_entry.get(): self.set_printer(kinematics, max_v, max_a, scv)
        printer_confirm_button.pack()
        parent.mainframe.pack()
        parent.window.mainloop()

    def set_printer(self, kinematics, max_vel=100, max_accel=1000, scv=5):

        self.printer.add_setting("kinematics", kinematics.get())
        self.printer.add_setting("max_velocity", max_vel)
        self.printer.add_setting("max_accel", max_accel)
        self.printer.add_setting("square_corner_velocity", scv)
        print("Printer: ", self.printer.get_output())
        recore = Recore(self.board)
        self.parent.add_config_section(recore.get_recore_config())
        self.parent.add_config_section(recore.get_mcu_config())
        self.parent.add_config_section(recore.get_mcu_ar100_config())
        self.parent.add_config_section(self.printer)
        self.parent.destroy_window()
        self.parent.stepper_config.create_stepper_section(self.parent, self.board.get())


    def return_to_board_selection_gui(self, parent):
        parent.destroy_window()
        parent.board_config.board_selection_gui(parent)
