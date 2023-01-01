import tkinter as tk
from ConfigSection import ConfigSection

RUN_CURRENT = "run_current"

STEALTHCHOP_THRESHOLD = "stealthchop_threshold"

HOMING_SPEED = "homing_speed"

POSITION_MAX = "position_max"

ENDSTOP = "position_endstop"

MICROSTEPS = "microsteps"

ROTATION_DISTANCE = "rotation_distance"


def get_stepper_possible_entries(parent):
    printer_config = None
    for config_section in parent.config:
        if config_section.get_name() == "printer":
            printer_config = config_section
            break

    match printer_config.get("kinematics"):
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


class StepperConfig:
    stepper_definition: ConfigSection
    driver_options: ConfigSection

    def __init__(self, parent):
        self.pin_map = None
        self.parent = parent

    def return_to_printer_gui(self, parent):
        parent.window.destroy()
        parent.create_printer_section()

    def create_stepper_section(self, parent):
        self.pin_map = parent.pin_map

        parent.create_window()
        return_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"), text="Back",
                                  width=5, height=5, bg="black", fg="white", command=self.return_to_printer_gui)
        return_button.pack()

        stepper_label = tk.Label(parent.mainframe, text="stepper name:")
        stepper_label.pack()

        stepper_label_options = get_stepper_possible_entries(parent)
        stepper_selected = tk.StringVar(parent.mainframe)
        stepper_selected.set(stepper_label_options[0])
        stepper_selection = tk.OptionMenu(parent.mainframe, stepper_selected, *stepper_label_options)
        stepper_selection.pack()

        stepper_connector_label = tk.Label(parent.mainframe,
                                           text="stepper connector (S6/S7 assumes a ReStep board plugged in):")
        stepper_connector_label.pack()

        stepper_connector = tk.StringVar(parent.mainframe)
        stepper_connector_options = self.pin_map.step_pin_map.keys()
        stepper_connector_selection = tk.OptionMenu(parent.mainframe, stepper_connector, *stepper_connector_options)
        stepper_connector_selection.pack()

        stepper_current_label = tk.Label(master=parent.mainframe, text="stepper current:")
        stepper_current_label.pack()
        stepper_current = "0.5"
        stepper_current_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10,
                                         textvariable=stepper_current)
        stepper_current_entry.insert(0, stepper_current)
        stepper_current_entry.pack()

        endstop_label = tk.Label(master=parent.mainframe, text="endstop connector")
        endstop_label.pack()

        endstop = tk.StringVar(parent.mainframe)
        endstop_options = self.pin_map.endstop_pin_map.keys()
        endstop_selection = tk.OptionMenu(parent.mainframe, endstop, *endstop_options)
        endstop_selection.pack()

        rotation_distance_label = tk.Label(master=parent.mainframe, text="rotation distance")
        rotation_distance_label.pack()
        rotation_distance = "40"
        rotation_distance_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white",
                                           textvariable=rotation_distance)
        rotation_distance_entry.insert(0, rotation_distance)
        rotation_distance_entry.pack()

        microstep_options = ["1", "2", "4", "8", "16", "32", "64", "128", "256"]
        microstep_label = tk.Label(master=parent.mainframe, text="microstep setting")
        microstep_label.pack()
        microstep = tk.StringVar(parent.mainframe)
        microstep_selection = tk.OptionMenu(parent.mainframe, microstep, *microstep_options)
        microstep_selection.pack()

        position_max_label = tk.Label(master=parent.mainframe, text="Maximum position (in mm)")
        position_max_label.pack()
        position_max = "200"
        position_max_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", textvariable=position_max)
        position_max_entry.insert(0, position_max)
        position_max_entry.pack()

        homing_speed_label = tk.Label(master=parent.mainframe, text="homing speed")
        homing_speed_label.pack()
        homing_speed = "100"
        homing_speed_entry = tk.Entry(master=parent.mainframe, textvariable=homing_speed)
        homing_speed_entry.insert(0, homing_speed)
        homing_speed_entry.pack()

        stealthchop_threshold_label = tk.Label(master=parent.mainframe, text="stealthchop threshold")
        stealthchop_threshold_label.pack()
        stealthchop_threshold = "99999"
        stealthchop_threshold_entry = tk.Entry(master=parent.mainframe, textvariable=stealthchop_threshold)
        stealthchop_threshold_entry.insert(0, stealthchop_threshold)
        stealthchop_threshold_entry.pack()

        add_another = tk.IntVar(master=parent.mainframe)
        add_another_box = tk.Checkbutton(master=parent.mainframe, text="add another stepper", variable=add_another)
        add_another_box.pack()

        stepper_confirm_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"),
                                           text="OK", width=5, height=5, bg="black", fg="white")
        stepper_confirm_button['command'] = lambda: self.set_stepper(stepper_label=stepper_selected.get(),
                                                                     stepper_connector=stepper_connector.get(),
                                                                     endstop_connector=endstop.get(),
                                                                     rotation_distance=rotation_distance_entry.get(),
                                                                     microstep=microstep.get(),
                                                                     position_max=position_max_entry.get(),
                                                                     run_current=stepper_current_entry.get(),
                                                                     homing_speed=homing_speed_entry.get(),
                                                                     stealthchop_threshold=stealthchop_threshold_entry.get(),
                                                                     another=bool(add_another.get()))
        stepper_confirm_button.pack()
        parent.mainframe.pack()
        parent.window.mainloop()

    def set_stepper(self, stepper_label, stepper_connector, endstop_connector, rotation_distance, microstep,
                    position_max, run_current, homing_speed, stealthchop_threshold, another):
        self.stepper_definition = ConfigSection(stepper_label)
        driver_label = "tmc2209 " + stepper_label
        self.driver_options = ConfigSection(driver_label)
        self.stepper_definition.add_setting("step_pin", self.pin_map.step_pin_map.get(stepper_connector))
        self.stepper_definition.add_setting("step_dir", self.pin_map.dir_pin_map.get(stepper_connector))
        self.stepper_definition.add_setting("endstop_pin", self.pin_map.endstop_pin_map.get(endstop_connector))
        self.stepper_definition.add_setting("%s" % ROTATION_DISTANCE, rotation_distance)
        self.stepper_definition.add_setting("%s" % MICROSTEPS, microstep)
        self.stepper_definition.add_setting("%s" % ENDSTOP, endstop_connector)
        self.stepper_definition.add_setting("%s" % POSITION_MAX, position_max)
        self.stepper_definition.add_setting("%s" % HOMING_SPEED, homing_speed)

        self.driver_options.add_setting("uart_pin", self.pin_map.uart_pin_map.get(stepper_connector))
        self.driver_options.add_setting("uart_address", self.pin_map.uart_address.get(stepper_connector))
        self.driver_options.add_setting("tx_pin", self.pin_map.tx_pin_map.get(stepper_connector))
        self.driver_options.add_setting("%s" % RUN_CURRENT, run_current)
        self.driver_options.add_setting("%s" % STEALTHCHOP_THRESHOLD, stealthchop_threshold)

        self.parent.add_config_section(self.driver_options)
        self.parent.add_config_section(self.stepper_definition)

        self.pin_map.step_pin_map.pop(stepper_connector, None)
        self.pin_map.dir_pin_map.pop(stepper_connector, None)
        self.pin_map.endstop_pin_map.pop(endstop_connector, None)
        self.pin_map.uart_address.pop(stepper_connector, None)
        self.pin_map.tx_pin_map.pop(stepper_connector, None)

        self.parent.window.destroy()
        if another:
            self.create_stepper_section(self.parent)
        else:
            self.parent.init_extruder()
            self.parent.extruder_config.create_extruder_section(self.parent)

    def get_stepper_config(self):
        return self.stepper_definition

    def get_stepper_options(self):
        return self.driver_options
