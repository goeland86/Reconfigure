import tkinter as tk
import tkinter.ttk as ttk
import configfile
from recore_pin_maps import RecoreA5PinMaps, RecoreA6PinMaps, RecoreA7PinMaps


class Reconfigure:
    border_effects = {"flat": tk.FLAT, "sunken": tk.SUNKEN, "raised": tk.RAISED, "groove": tk.GROOVE,
                      "ridge": tk.RIDGE}

    def __init__(self):
        self.board_selected = ""
        self.board_selection_gui()

    def board_selection_gui(self):
        self.window = tk.Tk()
        self.mainframe = tk.Frame(master=self.window)
        self.mainframe.pack()
        label = tk.Label(master=self.mainframe, relief=self.border_effects.get("ridge"),
                         text="Select the board to configure for:", height=10, fg="white", bg="black")
        label.pack()
        options = ["Recore A5", "Recore A6", "Recore A7"]
        board_selected = tk.StringVar(self.mainframe)
        board_selected.set(options[0])
        board_selection = tk.OptionMenu(self.mainframe, board_selected, *options)
        board_selection.pack()
        board_confirm_button = tk.Button(master=self.mainframe, relief=self.border_effects.get("groove"), text="Ok",
                                         width=5,
                                         height=5, bg="black", fg="white")
        board_confirm_button['command'] = lambda arg1=board_selected: self.set_board(arg1)
        board_confirm_button.pack()
        self.window.mainloop()

    def set_board(self, board):
        self.board_selected = board.get()
        print("board selected:", self.board_selected)
        self.mainframe.destroy()
        self.window.destroy()

    def create_printer_section(self):
        print("Beginning printer section")
        self.window = tk.Tk()
        self.mainframe = tk.Frame(master=self.window)

        # cartesian,
        #   corexy, corexz, hybrid_corexy, hybrid_corexz, rotary_delta, delta,
        #   deltesian, polar, winch, or none
        geometry_options = ["cartesian", "corexy", "corexz", "hybrid_corexy", "hybrid_corexz", "rotary_delta", "delta",
                            "deltesian", "polar", "winch", "none"]
        geometry_selected = tk.StringVar(self.mainframe)
        geometry_selected.set(geometry_options[0])
        geometry_selection = tk.OptionMenu(self.mainframe, geometry_selected, *geometry_options)
        geometry_selection.pack()
        max_velocity = "100"
        max_velocity_label = tk.Label(master=self.mainframe, text="Max velocity")
        max_velocity_entry = tk.Entry(master=self.mainframe, fg="black", bg="white", width=10, textvariable=max_velocity)
        max_velocity_entry.insert(index=0, string="100")
        max_velocity_label.pack()
        max_velocity_entry.pack()
        max_accel = "1000"
        max_accel_label=tk.Label(master=self.mainframe, text="Max Accel")
        max_accel_entry = tk.Entry(master=self.mainframe, fg="black", bg="white", width=10, textvariable=max_accel)
        max_accel_entry.insert(index=0, string="1000")
        max_accel_label.pack()
        max_accel_entry.pack()
        square_corner_velocity=5
        scv_label=tk.Label(master=self.mainframe, text="Square Corner Velocity")
        scv_entry = tk.Entry(master=self.mainframe, fg="black", bg="white", width=10, textvariable=square_corner_velocity)
        scv_entry.insert(0, square_corner_velocity)
        scv_label.pack()
        scv_entry.pack()
        printer_confirm_button = tk.Button(master=self.mainframe, relief=self.border_effects.get("groove"), text="Ok",
                                           width=5,
                                           height=5, bg="black", fg="white")
        printer_confirm_button['command'] = \
            lambda kinematics=geometry_selected: self.set_printer(kinematics, max_velocity, max_accel)
        printer_confirm_button.pack()
        self.mainframe.pack()
        self.window.mainloop()

    def set_printer(self, kinematics, max_vel=100, max_accel=1000, scv=5):
        self.printer = {"kinematics": kinematics.get(),
                        "max_velocity": max_vel,
                        "max_accel": max_accel,
                        "square_corner_velocity": scv
                        }
        print("Printer: ", self.printer)
        self.mainframe.destroy()
        self.window.destroy()


main = Reconfigure()
main.create_printer_section()

#main.window.quit()
