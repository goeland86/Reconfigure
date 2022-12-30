import tkinter as tk
import ConfigSection
from Recore_pin_maps import *

RUN_CURRENT = "run_current"

STEALTHCHOP_THRESHOLD = "stealthchop_threshold"

HOMING_SPEED = "homing_speed"

POSITION_MAX = "position_max"

ENDSTOP = "position_endstop"

MICROSTEPS = "microsteps"

ROTATION_DISTANCE = "rotation_distance"


def get_stepper_possible_entries(parent):
    match parent.printer_config.get_printer_config().get("kinematics"):
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
    _stepper_type = "stepper"
    _driver_type = "driver"
    stepper_definition: ConfigSection
    driver_options: ConfigSection

    def __init__(self, parent, ):
        self.pin_map = None
        self.parent = parent

    def return_to_printer_gui(self, parent):
        parent.window.destroy()
        parent.create_printer_section()

    def create_stepper_section(self, parent, board):
        if board == "Recore A5":
            self.pin_map = RecoreA5PinMaps()
        elif board == "Recore A6":
            self.pin_map = RecoreA6PinMaps()
        elif board == "Recore A7":
            self.pin_map = RecoreA7PinMaps()

        parent.create_window()
        return_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"), text="Back",
                                  width=5, height=5, bg="black", fg="white", command=self.return_to_printer_gui)
        return_button.pack()
        stepper_label = tk.Label(parent.mainframe, text="stepper name:")
        stepper_label.pack()
        stepper_label_options = get_stepper_possible_entries()
        stepper_selected = tk.StringVar(parent.mainframe)
        stepper_selected.set(stepper_label_options[0])
        stepper_selection = tk.OptionMenu(parent.mainframe, stepper_selected, *stepper_label_options)
        stepper_selection.pack()

        stepper_connector_label = tk.Label(text="stepper connector (S6/S7 assumes a ReStep board plugged in):")
        stepper_connector_label.pack()
        stepper_connector = tk.StringVar(parent.mainframe)
        stepper_connector_options = ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7"]
        stepper_connector_selection = tk.OptionMenu(parent.mainframe, stepper_connector, *stepper_connector_options)
        stepper_connector_selection.pack()

        stepper_current_label = tk.Label(master=parent.mainframe, text="stepper current:")
        stepper_current_label.pack()
        stepper_current = "0.5"
        stepper_current_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10,
                                         textvariable=stepper_current)
        stepper_current_entry.insert(0, stepper_current)
        stepper_current_entry.pack()

        # TODO add entries for stepper values, and add to self.steppers dict.
        stepper_options = dict()
        stepper_settings = dict()

        stepper_confirm_button = tk.Button(master=parent.mainframe, relief=self.border_effects.get("groove"), text="OK",
                                           width=5, height=5, bg="black", fg="white")
        stepper_confirm_button['command'] = lambda stepper_label=stepper_selected.get(), \
                                                   connector=stepper_connector.get(), \
                                                   options=stepper_options, \
                                                   settings=stepper_settings: \
            self.set_stepper(stepper_label, connector, options, settings)
        stepper_confirm_button.pack()
        parent.mainframe.pack()
        parent.window.mainloop()

    def set_stepper(self, stepper_label, stepper_connector, endstop_connector, stepper_settings, driver_options):
        self.stepper_definition = ConfigSection(stepper_label, self._stepper_type)
        driver_label = "tmc2209 " + stepper_label
        self.driver_options = ConfigSection(driver_label, self._driver_type)
        # TODO do the magic of fetching the pin options for the right connector
        self.stepper_definition.add_setting("step_pin", self.pin_map.step_pin_map.get(stepper_connector))
        self.stepper_definition.add_setting("step_dir", self.pin_map.dir_pin_map.get(stepper_connector))
        self.stepper_definition.add_setting("endstop_pin", self.pin_map.endstop_pin_map.get(endstop_connector))
        self.stepper_definition.add_setting("%s" % ROTATION_DISTANCE, stepper_settings.get(ROTATION_DISTANCE))
        self.stepper_definition.add_setting("%s" % MICROSTEPS, stepper_settings.get(MICROSTEPS))
        self.stepper_definition.add_setting("%s" % ENDSTOP, stepper_settings.get(ENDSTOP))
        self.stepper_definition.add_setting("%s" % POSITION_MAX, stepper_settings.get(POSITION_MAX))
        self.stepper_definition.add_setting("%s" % HOMING_SPEED, stepper_settings.get(HOMING_SPEED))

        self.driver_options.add_setting("uart_pin", self.pin_map.uart_pin_map.get(stepper_connector))
        self.driver_options.add_setting("uart_address", self.pin_map.uart_address_map.get(stepper_connector))
        self.driver_options.add_setting("tx_pin", self.pin_map.tx_pin_map.get(stepper_connector))
        self.driver_options.add_setting("%s" % RUN_CURRENT, driver_options.get(RUN_CURRENT))
        self.driver_options.add_setting("%s" % STEALTHCHOP_THRESHOLD, driver_options.get(STEALTHCHOP_THRESHOLD))

    def get_stepper_config(self):
        return self.stepper_definition

    def get_stepper_options(self):
        return self.driver_options
