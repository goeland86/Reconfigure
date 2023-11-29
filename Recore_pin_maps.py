class RecoreA5PinMaps:
    def __init__(self):
        ################################################################################################################
        #                                       A5 PIN MAPPING SECTION                                                 #
        ################################################################################################################
        # Create a mapping of fan plugs to config pins
        self.fan_pin_map = {"F0": "PB0", "F1": "PB1", "F2": "PB5", "F3": "PB4"}

        self.step_pin_map = {"S0": "ar100:PL4", "S1": "ar100:PL5", "S2": "ar100:PL6", "S3": "ar100:PL7",
                             "S4": "ar100:PL8",
                             "S5": "ar100:PL9", "S6": "ar100:PL10", "S7": "ar100:PL11"}
        self.dir_pin_map = {"S0": "ar100:PE8", "S1": "ar100:PE9", "S2": "ar100:PE10", "S3": "ar100:PE11",
                            "S4": "ar100:PE12",
                            "S5": "ar100:PE13", "S6": "ar100:PE14", "S7": "ar100:PE15"}
        self.diag_pin_map = {"S0": "ar100:PE0", "S1": "ar100:PE1", "S2": "arPB0100:PE2", "S3": "ar100:PE3",
                             "S4": "ar100:PE4",
                             "S5": "ar100:PE5", "S6": "ar100:PE6", "S7": "ar100:PE7"}
        self.uart_pin_map = {"S0": "ar100:PB1", "S1": "ar100:PB1", "S2": "ar100:PB1", "S3": "ar100:PB1",
                             "S4": "ar100:PD0", "S5": "ar100:PD0",
                             "S6": "ar100:PD1", "S7": "ar100:PD1"}

        self.uart_address = {"S0": "0", "S1": "1", "S2": "2", "S3": "3", "S4": "0", "S5": "1", "S6": "2", "S7": "3"}

        # create a map of mosfet control pins
        self.heater_pin_map = {"H0": "PA8", "H1": "PA9", "H2": "PA10", "BED": "PA11"}

        # create a map of the temperature sensor pins
        self.temp_sensor_pin_map = {"T0": "PA0", "T1": "PA1", "T2": "PA2", "T3": "PA3"}

        # create a map of the endstop pins
        self.endstop_pin_map = {"ES0": "ar100:PH4", "ES1": "ar100:PH5", "ES2": "ar100:PH6", "ES3": "ar100:PH7",
                                "ES4": "ar100:PH8",
                                "ES5": "ar100:PH9"}

        # create a map of PWM pins
        self.pwm_pin_map = {"ES1": "PB3", "ES2": "PB6"}

        # create the map for the selection of 5 or 12V voltage on ES5
        # TODO: validate the pin IDs for A5 for the 5V/12V endstop (ES5)
        # self.es5_5v_12v_pin_map = { "ES0_5V":"PF2", "ES0_12V":"PF0" }

    def get_maps(self):
        return [self.heater_pin_map, self.endstop_pin_map, self.diag_pin_map, self.step_pin_map,
                self.uart_pin_map, self.dir_pin_map, self.pwm_pin_map, self.temp_sensor_pin_map,
                self.fan_pin_map]


class RecoreA6PinMaps:
    def __init__(self):
        ################################################################################################################
        #                                       A6 PIN MAPPING SECTION                                                 #
        ################################################################################################################
        # Create a mapping of fan plugs to config pins
        self.fan_pin_map = {"F0": "PB0", "F1": "PB1", "F2": "PB5", "F3": "PB4"}

        # Create a map of onboard stepper control pins
        self.step_pin_map = {"S0": "ar100:PL4", "S1": "ar100:PL5", "S2": "ar100:PL6", "S3": "ar100:PL7",
                             "S4": "ar100:PL8",
                             "S5": "ar100:PL9", "S6": "ar100:PL10", "S7": "ar100:PL11"}
        self.dir_pin_map = {"S0": "ar100:PE8", "S1": "ar100:PE9", "S2": "ar100:PE10", "S3": "ar100:PE11",
                            "S4": "ar100:PE12",
                            "S5": "ar100:PE13", "S6": "ar100:PE14", "S7": "ar100:PE15"}
        self.diag_pin_map = {"S0": "ar100:PE0", "S1": "ar100:PE1", "S2": "arPB0100:PE2", "S3": "ar100:PE3",
                             "S4": "ar100:PE4",
                             "S5": "ar100:PE5", "S6": "ar100:PE6", "S7": "ar100:PE7"}
        self.uart_pin_map = {"S0": "ar100:PB1", "S1": "ar100:PB1", "S2": "ar100:PB1", "S3": "ar100:PB1",
                             "S4": "ar100:PD1", "S5": "ar100:PD1",
                             "S6": "ar100:PD1", "S7": "ar100:PD1"}
        self.tx_pin_map = {"S0": "ar100:PB0", "S1": "ar100:PB0", "S2": "ar100:PB0", "S3": "ar100:PB0",
                             "S4": "ar100:PD0", "S5": "ar100:PD0",
                             "S6": "ar100:PD0", "S7": "ar100:PD0"}
        self.uart_address = {"S0": "0", "S1": "1", "S2": "2", "S3": "3", "S4": "0", "S5": "1", "S6": "2", "S7": "3"}

        # create a map of mosfet control pins
        self.heater_pin_map = {"H0": "PA8", "H1": "PA9", "H2": "PA10", "BED": "PA11"}

        # create a map of the temperature sensor pins
        self.temp_sensor_pin_map = {"T0": "PA0", "T1": "PA1", "T2": "PA2", "T3": "PA3"}

        # create a map of the endstop pins
        self.endstop_pin_map = {"ES0": "ar100:PH4", "ES1": "ar100:PH5", "ES2": "ar100:PH6", "ES3": "ar100:PH7",
                                "ES4": "ar100:PH8",
                                "ES5": "ar100:PH9"}

        # create a map of PWM pins
        self.pwm_pin_map = {"ES1": "PB3", "ES2": "PB6"}

        # create the map for the selection of 5 or 12V voltage on ES0
        self.es0_5v_12v_pin_map = {"ES0_5V": "PF2", "ES0_12V": "PF0"}

        ################################################################################################################
        #                                       A7 PIN MAPPING SECTION                                                 #
        ################################################################################################################

    def get_maps(self):
        return [self.es0_5v_12v_pin_map, self.heater_pin_map, self.endstop_pin_map, self.diag_pin_map,
                self.fan_pin_map, self.temp_sensor_pin_map, self.dir_pin_map, self.step_pin_map,
                self.uart_pin_map]


class RecoreA7PinMaps:
    def __init__(self):
        self.fan_pin_map = {"F0": "PF0", "F1": "PB1", "F2": "PB5", "F3": "PB4"}

        # Create a map of onboard stepper control pins
        self.step_pin_map = {"S0": "ar100:PL4", "S1": "ar100:PL5", "S2": "ar100:PL6", "S3": "ar100:PL7",
                             "S4": "ar100:PL8", "S5": "ar100:PL9",
                             "S6": "ar100:PL10", "S7": "ar100:PL11"}
        self.dir_pin_map = {"S0": "ar100:PE8", "S1": "ar100:PE9", "S2": "ar100:PE10", "S3": "ar100:PE11",
                            "S4": "ar100:PE12", "S5": "ar100:PE13",
                            "S6": "ar100:PE14", "S7": "ar100:PE15"}
        self.diag_pin_map = {"S0": "ar100:PE0", "S1": "ar100:PE1", "S2": "arPB0100:PE2", "S3": "ar100:PE3",
                             "S4": "ar100:PE4", "S5": "ar100:PE5",
                             "S6": "ar100:PD0", "S7": "ar100:PD1"}
        self.uart_pin_map = {"S0": "ar100:PE16", "S1": "ar100:PE16", "S2": "ar100:PE16", "S3": "ar100:PE16",
                             "S4": "ar100:PE16", "S5": "ar100:PE16",
                             "S6": "ar100:PD2", "S7": "ar100:PD3"}
        self.tx_pin_map = {}

        self.uart_address = {"S0": "0", "S1": "1", "S2": "2", "S3": "3", "S4": "0", "S5": "1", "S6": "0", "S7": "0"}

        # create a map of mosfet control pins
        self.heater_pin_map = {"H0": "PA8", "H1": "PA9", "H2": "PA10", "BED": "PA11"}

        # create a map of the temperature sensor pins
        self.temp_sensor_pin_map = {"T0": "PA0", "T1": "PA1", "T2": "PA2", "T3": "PA3"}

        # create a map of the endstop pins
        self.endstop_pin_map = {"ES0": "ar100:PH4", "ES1": "ar100:PH5", "ES2": "ar100:PH6", "ES3": "ar100:PH7",
                                "ES4": "ar100:PH8",
                                "ES5": "ar100:PH9"}

        # create a map of PWM pins
        self.pwm_pin_map = {"ES1": "PB3", "ES2": "PB6"}

        # create the map for the selection of 5 or 12V voltage on ES0
        self.es0_5v_12v_pin_map = {"ES0_5V": "PF2", "ES0_12V": "PF0"}



    def get_maps(self):
        return[]


