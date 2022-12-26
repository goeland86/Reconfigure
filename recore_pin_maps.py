class RecoreA5PinMaps:
    def __init__(self):
        ################################################################################################################
        #                                       A5 PIN MAPPING SECTION                                                 #
        ################################################################################################################
        # Create a mapping of fan plugs to config pins
        self.a5_fan_pin_map = {"F0": "PB0", "F1": "PB1", "F2": "PB5", "F3": "PB4"}

        self.a5_step_pin_map = {"S0": "ar100:PL4", "S1": "ar100:PL5", "S2": "ar100:PL6", "S3": "ar100:PL7",
                                "S4": "ar100:PL8",
                                "S5": "ar100:PL9", "S6": "ar100:PL10", "S7": "ar100:PL11"}
        self.a5_dir_pin_map = {"S0": "ar100:PE8", "S1": "ar100:PE9", "S2": "ar100:PE10", "S3": "ar100:PE11",
                               "S4": "ar100:PE12",
                               "S5": "ar100:PE13", "S6": "ar100:PE14", "S7": "ar100:PE15"}
        self.a5_diag_pin_map = {"S0": "ar100:PE0", "S1": "ar100:PE1", "S2": "arPB0100:PE2", "S3": "ar100:PE3",
                                "S4": "ar100:PE4",
                                "S5": "ar100:PE5", "S6": "ar100:PE6", "S7": "ar100:PE7"}
        self.a5_uart_pin_map = {"S0": "ar100:PB1", "S1": "ar100:PB1", "S2": "ar100:PB1", "S3": "ar100:PB1",
                                "S4": "ar100:PD0", "S5": "ar100:PD0",
                                "S6": "ar100:PD1", "S7": "ar100:PD1"}

        # create a map of mosfet control pins
        self.a5_heater_pin_map = {"H0": "PA8", "H1": "PA9", "H2": "PA10", "Bed": "PA11"}

        # create a map of the temperature sensor pins
        self.a5_temp_sensor_pin_map = {"T0": "PA0", "T1": "PA1", "T2": "PA2", "T3": "PA3"}

        # create a map of the endstop pins
        self.a5_endstop_pin_map = {"ES0": "ar100:PH4", "ES1": "ar100:PH5", "ES2": "ar100:PH6", "ES3": "ar100:PH7",
                                   "ES4": "ar100:PH8",
                                   "ES5": "ar100:PH9"}

        # create a map of PWM pins
        self.a5_pwm_pin_map = {"ES1": "PB3", "ES2": "PB6"}

        # create the map for the selection of 5 or 12V voltage on ES5
        # TODO: validate the pin IDs for A5 for the 5V/12V endstop (ES5)
        # self.a5_es5_5v_12v_pin_map = { "ES0_5V":"PF2", "ES0_12V":"PF0" }

    def get_maps(self):
        return [self.a5_heater_pin_map, self.a5_endstop_pin_map, self.a5_diag_pin_map, self.a5_step_pin_map,
                self.a5_uart_pin_map, self.a5_dir_pin_map, self.a5_pwm_pin_map, self.a5_temp_sensor_pin_map,
                self.a5_fan_pin_map]


class RecoreA6PinMaps:
    def __init__(self):
        ################################################################################################################
        #                                       A6 PIN MAPPING SECTION                                                 #
        ################################################################################################################
        # Create a mapping of fan plugs to config pins
        self.a6_fan_pin_map = {"F0": "PB0", "F1": "PB1", "F2": "PB5", "F3": "PB4"}

        # Create a map of onboard stepper control pins
        self.a6_step_pin_map = {"S0": "ar100:PL4", "S1": "ar100:PL5", "S2": "ar100:PL6", "S3": "ar100:PL7",
                                "S4": "ar100:PL8",
                                "S5": "ar100:PL9", "S6": "ar100:PL10", "S7": "ar100:PL11"}
        self.a6_dir_pin_map = {"S0": "ar100:PE8", "S1": "ar100:PE9", "S2": "ar100:PE10", "S3": "ar100:PE11",
                               "S4": "ar100:PE12",
                               "S5": "ar100:PE13", "S6": "ar100:PE14", "S7": "ar100:PE15"}
        self.a6_diag_pin_map = {"S0": "ar100:PE0", "S1": "ar100:PE1", "S2": "arPB0100:PE2", "S3": "ar100:PE3",
                                "S4": "ar100:PE4",
                                "S5": "ar100:PE5", "S6": "ar100:PE6", "S7": "ar100:PE7"}
        self.a6_uart_pin_map = {"S0": "ar100:PB1", "S1": "ar100:PB1", "S2": "ar100:PB1", "S3": "ar100:PB1",
                                "S4": "ar100:PD0", "S5": "ar100:PD0",
                                "S6": "ar100:PD1", "S7": "ar100:PD1"}

        # create a map of mosfet control pins
        self.a6_heater_pin_map = {"H0": "PA8", "H1": "PA9", "H2": "PA10", "Bed": "PA11"}

        # create a map of the temperature sensor pins
        self.a6_temp_sensor_pin_map = {"T0": "PA0", "T1": "PA1", "T2": "PA2", "T3": "PA3"}

        # create a map of the endstop pins
        self.a6_endstop_pin_map = {"ES0": "ar100:PH4", "ES1": "ar100:PH5", "ES2": "ar100:PH6", "ES3": "ar100:PH7",
                                   "ES4": "ar100:PH8",
                                   "ES5": "ar100:PH9"}

        # create a map of PWM pins
        self.a6_pwm_pin_map = {"ES1": "PB3", "ES2": "PB6"}

        # create the map for the selection of 5 or 12V voltage on ES0
        self.a6_es0_5v_12v_pin_map = {"ES0_5V": "PF2", "ES0_12V": "PF0"}

        ################################################################################################################
        #                                       A7 PIN MAPPING SECTION                                                 #
        ################################################################################################################

    def get_maps(self):
        return [self.a6_es0_5v_12v_pin_map, self.a6_heater_pin_map, self.a6_endstop_pin_map, self.a6_diag_pin_map,
                self.a6_fan_pin_map, self.a6_temp_sensor_pin_map, self.a6_dir_pin_map, self.a6_step_pin_map,
                self.a6_uart_pin_map]


class RecoreA7PinMaps:
    def __init__(self):
        print("WARNING: The A7 pin maps have not yet been implemented as the board design is not yet finalized.")
        print("Therefore the pin assignment used will be for an A6 revision board.")

    def get_maps(self):
        a6_maps = RecoreA6PinMaps()
        return a6_maps.get_a6_maps()
