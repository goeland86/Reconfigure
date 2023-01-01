import tkinter as tk
from ConfigSection import ConfigSection

RUN_CURRENT = "run_current"
STEALTHCHOP_THRESHOLD = "stealthchop_threshold"
HOMING_SPEED = "homing_speed"
POSITION_MAX = "position_max"
ENDSTOP = "position_endstop"
MICROSTEPS = "microsteps"
ROTATION_DISTANCE = "rotation_distance"
NOZZLE_DIAMETER = "nozzle_diameter"
FILAMENT_DIAMETER = "filament_diameter"
SENSOR_TYPE = "sensor_type"


def get_extruder_possible_entries():
    return ["extruder", "extruder1", "extruder2"]


class ExtruderConfig:
    stepper_definition: ConfigSection
    driver_options: ConfigSection

    def __init__(self, parent):
        self.parent = parent
        self.pin_map = None

    def return_to_stepper_gui(self, parent):
        parent.window.destroy()
        parent.stepper_config.create_stepper_section()

    def create_extruder_section(self, parent):
        self.pin_map = parent.pin_map

        parent.create_window()
        return_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"), text="Back",
                                  width=5, height=5, bg="black", fg="white", command=self.return_to_stepper_gui)
        return_button.pack()

        stepper_label = tk.Label(parent.mainframe, text="extruder name:")
        stepper_label.pack()

        stepper_label_options = get_extruder_possible_entries()
        stepper_selected = tk.StringVar(parent.mainframe)
        stepper_selected.set(stepper_label_options[0])
        stepper_selection = tk.OptionMenu(parent.mainframe, stepper_selected, *stepper_label_options)
        stepper_selection.pack()

        stepper_connector_label = tk.Label(parent.mainframe,
                                           text="extruder stepper connector (S6/S7 assumes a ReStep board plugged in):")
        stepper_connector_label.pack()

        stepper_connector = tk.StringVar(parent.mainframe)
        stepper_connector_options = self.pin_map.step_pin_map.keys()
        stepper_connector_selection = tk.OptionMenu(parent.mainframe, stepper_connector, *stepper_connector_options)
        stepper_connector_selection.pack()

        stepper_current_label = tk.Label(master=parent.mainframe, text="extruder current:")
        stepper_current_label.pack()
        stepper_current = "0.5"
        stepper_current_entry = tk.Entry(master=parent.mainframe, fg="black", bg="white", width=10,
                                         textvariable=stepper_current)
        stepper_current_entry.insert(0, stepper_current)
        stepper_current_entry.pack()

        sensor_pin_label = tk.Label(master=parent.mainframe, text="sensor connector")
        sensor_pin_label.pack()

        sensor_pin = tk.StringVar(master=parent.mainframe)
        sensor_pin_options = self.pin_map.temp_sensor_pin_map.keys()
        sensor_pin_selection = tk.OptionMenu(parent.mainframe, sensor_pin, *sensor_pin_options)
        sensor_pin_selection.pack()

        sensor_type_label = tk.Label(master=parent.mainframe, text="temperature sensor type")
        sensor_type_label.pack()

        sensor_type = tk.StringVar(master=parent.mainframe)
        sensor_type_options = ["EPCOS 100K B57560G104F", "ATC Semitec 104GT-2", "ATC Semitec 104NT-4-R025H42G",
                               "Generic 3950", "Honeywell 100K 135-104LAG-J01", "NTC 100K MGB18-104F39050L32",
                               "SliceEngineering 450", "TDK NTCG104LH104JT1"]
        sensor_type_selection = tk.OptionMenu(parent.mainframe, sensor_type, *sensor_type_options)
        sensor_type_selection.pack()

        heater_pin_label = tk.Label(master=parent.mainframe, text="heater connector")
        heater_pin_label.pack()

        heater_pin = tk.StringVar(parent.mainframe)
        heater_pin_options = self.pin_map.heater_pin_map.keys()
        heater_selection = tk.OptionMenu(parent.mainframe, heater_pin, *heater_pin_options)
        heater_selection.pack()

        nozzle_diameter_label = tk.Label(master=parent.mainframe, text="nozzle diameter")
        nozzle_diameter_label.pack()

        nozzle_diameter = "0.4"
        nozzle_diameter_entry = tk.Entry(master=parent.mainframe, textvariable=nozzle_diameter)
        nozzle_diameter_entry.insert(0, nozzle_diameter)
        nozzle_diameter_entry.pack()

        filament_diameter_label = tk.Label(master=parent.mainframe, text="filament diameter")
        filament_diameter_label.pack()

        filament_diameter = "1.75"
        filament_diameter_entry = tk.Entry(master=parent.mainframe, textvariable=filament_diameter)
        filament_diameter_entry.insert(0, filament_diameter)
        filament_diameter_entry.pack()

        min_temp_label = tk.Label(master=parent.mainframe, text="Mininmum temperature")
        min_temp_label.pack()

        min_temp = "10"
        min_temp_entry = tk.Entry(master=parent.mainframe, textvariable=min_temp)
        min_temp_entry.insert(0, min_temp)
        min_temp_entry.pack()

        max_temp_label = tk.Label(master=parent.mainframe, text="Mininmum temperature")
        max_temp_label.pack()

        max_temp = "300"
        max_temp_entry = tk.Entry(master=parent.mainframe, textvariable=max_temp)
        max_temp_entry.insert(0, max_temp)
        max_temp_entry.pack()

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

        stealthchop_threshold_label = tk.Label(master=parent.mainframe, text="stealthchop threshold")
        stealthchop_threshold_label.pack()
        stealthchop_threshold = "99999"
        stealthchop_threshold_entry = tk.Entry(master=parent.mainframe, textvariable=stealthchop_threshold)
        stealthchop_threshold_entry.insert(0, stealthchop_threshold)
        stealthchop_threshold_entry.pack()

        add_another = tk.IntVar(master=parent.mainframe)
        add_another_box = tk.Checkbutton(master=parent.mainframe, text="add another extruder", variable=add_another)
        add_another_box.pack()

        extruder_confirm_button = tk.Button(master=parent.mainframe, relief=parent.border_effects.get("groove"),
                                            text="OK", width=5, height=5, bg="black", fg="white")
        extruder_confirm_button['command'] = lambda: self.set_extruder(stepper_label=stepper_selected.get(),
                                                                       stepper_connector=stepper_connector.get(),
                                                                       sensor_connector=sensor_pin.get(),
                                                                       rotation_distance=rotation_distance_entry.get(),
                                                                       microstep=microstep.get(),
                                                                       run_current=stepper_current_entry.get(),
                                                                       stealthchop_threshold=stealthchop_threshold_entry.get(),
                                                                       sensor_type=sensor_type.get(),
                                                                       filament_diameter=filament_diameter_entry.get(),
                                                                       heater_connector=heater_pin.get(),
                                                                       nozzle_diameter=nozzle_diameter_entry.get(),
                                                                       min_temp=min_temp_entry.get(),
                                                                       max_temp=max_temp_entry.get(),
                                                                       another=bool(add_another.get()))
        extruder_confirm_button.pack()
        parent.mainframe.pack()
        parent.window.mainloop()

    def set_extruder(self, stepper_label, stepper_connector, sensor_connector, sensor_type, rotation_distance,
                     microstep, min_temp, max_temp,
                     filament_diameter, nozzle_diameter, run_current, heater_connector, stealthchop_threshold, another):
        self.stepper_definition = ConfigSection(stepper_label)
        driver_label = "tmc2209 " + stepper_label
        self.driver_options = ConfigSection(driver_label)
        self.stepper_definition.add_setting("step_pin", self.pin_map.step_pin_map.get(stepper_connector))
        self.pin_map.step_pin_map.pop(stepper_connector, None)
        self.stepper_definition.add_setting("step_dir", self.pin_map.dir_pin_map.get(stepper_connector))
        self.pin_map.dir_pin_map.pop(stepper_connector, None)
        self.stepper_definition.add_setting("%s" % ROTATION_DISTANCE, rotation_distance)
        self.stepper_definition.add_setting("%s" % MICROSTEPS, microstep)
        self.stepper_definition.add_setting("%s" % SENSOR_TYPE, sensor_type)
        self.stepper_definition.add_setting("%s" % FILAMENT_DIAMETER, filament_diameter)
        self.stepper_definition.add_setting("%s" % NOZZLE_DIAMETER, nozzle_diameter)
        self.stepper_definition.add_setting("sensor_pin", self.pin_map.temp_sensor_pin_map.get(sensor_connector))
        self.pin_map.temp_sensor_pin_map.pop(sensor_connector, None)
        self.stepper_definition.add_setting("heater_pin", self.pin_map.heater_pin_map.get(heater_connector))
        self.pin_map.heater_pin_map.pop(heater_connector, None)
        self.stepper_definition.add_setting("min_temp", min_temp)
        self.stepper_definition.add_setting("max_temp", max_temp)
        self.stepper_definition.add_setting("control", "pid")
        self.stepper_definition.add_setting("pid_Kp", '22.2')
        self.stepper_definition.add_setting("pid_Ki", "1.08")
        self.stepper_definition.add_setting("pid_Kd", "114")

        self.driver_options.add_setting("uart_pin", self.pin_map.uart_pin_map.get(stepper_connector))
        self.pin_map.uart_pin_map.pop(stepper_connector, None)
        self.driver_options.add_setting("uart_address", self.pin_map.uart_address.get(stepper_connector))
        self.pin_map.uart_address.pop(stepper_connector, None)
        self.driver_options.add_setting("tx_pin", self.pin_map.tx_pin_map.get(stepper_connector))
        self.pin_map.tx_pin_map.pop(stepper_connector, None)
        self.driver_options.add_setting("%s" % RUN_CURRENT, run_current)
        self.driver_options.add_setting("%s" % STEALTHCHOP_THRESHOLD, stealthchop_threshold)

        self.parent.add_config_section(self.driver_options)
        self.parent.add_config_section(self.stepper_definition)

        self.parent.window.destroy()
        if another:
            self.create_extruder_section(self.parent, self.board)
        else:
            print("End of the wizard for now.")

    def get_stepper_config(self):
        return self.stepper_definition

    def get_stepper_options(self):
        return self.driver_options
