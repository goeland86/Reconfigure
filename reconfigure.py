import tkinter as tk
from recore_pin_maps import RecoreA5PinMaps, RecoreA6PinMaps, RecoreA7PinMaps


class Reconfigure:
    border_effects = {"flat": tk.FLAT, "sunken": tk.SUNKEN, "raised": tk.RAISED, "groove": tk.GROOVE,
                      "ridge": tk.RIDGE}

    def __init__(self):
        self.board_selected = ""
        self.steppers = dict()

    def create_window(self):
        self.window = tk.Tk()
        self.mainframe = tk.Frame(master=self.window, width=400, height=400, relief=self.border_effects.get("raised"))
        self.mainframe.pack()

    def board_selection_gui(self):
        self.create_window()
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
        self.create_printer_section()

    def return_to_board_selection_gui(self):
        self.mainframe.destroy()
        self.window.destroy()
        self.board_selection_gui()

    def create_printer_section(self):
        self.create_window()
        return_button = tk.Button(master=self.mainframe, relief=self.border_effects.get("groove"), text="Back",
                                           width=5,
                                           height=5, bg="black", fg="white")
        return_button['command'] = self.return_to_board_selection_gui
        return_button.pack()
        # list of options taken from https://www.klipper3d.org/Config_Reference.html#printer
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
        self.create_stepper_section()


    def return_to_printer_gui(self):
        self.window.destroy()
        self.create_printer_section()

    def create_stepper_section(self):
        self.create_window()
        return_button = tk.Button(master=self.mainframe, relief=self.border_effects.get("groove"), text="Back",
                                  width=5,
                                  height=5, bg="black", fg="white", command=self.return_to_printer_gui)
        return_button.pack()
        stepper_label = tk.Label(self.mainframe,text="stepper name:")
        stepper_label.pack()
        stepper_label_options = self.get_stepper_possible_entries()
        stepper_selected = tk.StringVar(self.mainframe)
        stepper_selected.set(stepper_label_options[0])
        stepper_selection = tk.OptionMenu(self.mainframe,stepper_selected, *stepper_label_options)
        stepper_selection.pack()

        stepper_connector_label = tk.Label(text="stepper connector (S6/S7 assumes a ReStep board plugged in):")
        stepper_connector_label.pack()
        stepper_connector = tk.StringVar(self.mainframe)
        stepper_connector_options = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]
        stepper_connector_selection = tk.OptionMenu(self.mainframe, stepper_connector, *stepper_connector_options)
        stepper_connector_selection.pack()

        stepper_current_label = tk.Label(master=self.mainframe, text="stepper current:")
        stepper_current_label.pack()
        stepper_current = "0.5"
        stepper_current_entry = tk.Entry(master=self.mainframe, fg="black", bg="white", width=10,
                                         textvariable=stepper_current)
        stepper_current_entry.insert(0,stepper_current)
        stepper_current_entry.pack()

        # TODO add entries for stepper values, and add to self.steppers dict.
        stepper_options=dict()
        stepper_settings=dict()

        stepper_confirm_button = tk.Button(master=self.mainframe, relief=self.border_effects.get("groove"), text="OK",
                                           width=5, height=5, bg="black", fg="white")
        stepper_confirm_button['command'] = lambda stepper_label=stepper_selected.get(), \
                                                   connector=stepper_connector.get(),\
                                                   options=stepper_options, \
                                                   settings=stepper_settings : \
            self.set_stepper(stepper_label, connector, options, settings)
        stepper_confirm_button.pack()
        self.mainframe.pack()
        self.window.mainloop()

    def set_stepper(self, stepper_label, stepper_connector, stepper_options, stepper_settings):
        # TODO some fancy magic with pin maps from the recore_pin_maps based on the connector
        self.steppers.update(stepper_label, stepper_options)
        self.stepper_options.update(stepper_label, stepper_settings)

    def get_stepper_possible_entries(self):
        match self.printer.get("kinematics"):
            case "cartesian":
                return ["stepper_x", "stepper_y", "stepper_z", "stepper_z2", "stepper_x2", "stepper_y2"]
            case "corexy":
                return ["stepper_x", "stepper_y", "stepper_z", "stepper_z2", "stepper_x2", "stepper_y2"]
            case "corexz":
                return ["stepper_x", "stepper_y", "stepper_z", "stepper_z2", "stepper_x2", "stepper_y2"]
            case "hybrid_corexy":
                return ["stepper_x", "stepper_y", "stepper_z", "stepper_z2", "stepper_x2", "stepper_y2"]
            case "hybrid_corexz":
                return ["stepper_x", "stepper_y", "stepper_z", "stepper_z2", "stepper_x2", "stepper_y2"]
            case "delta":
                return ["stepper_a", "stepper_b", "stepper_c"]
            case "deltesian":
                return ["stepper_left", "stepper_right", "stepper_y"]
            case "polar":
                return ["stepper_bed", "stepper_arm", "stepper_z"]
            case "rotary_delta":
                return ["stepper_a", "stepper_b", "stepper_c"]
            case "winch":
                return ["stepper_a", "stepper_b", "stepper_c", "stepper_d"]


main = Reconfigure()

main.board_selection_gui()
#main.window.quit()
