import ConfigSection


class RecoreConfig:
    recore: ConfigSection
    mcu: ConfigSection
    mcu_ar100: ConfigSection

    def __init__(self, board):
        self.recore = ConfigSection("recore")
        self.mcu = ConfigSection("mcu")
        self.mcu_ar100 = ConfigSection("mcu ar100")
        match board:
            case "Recore A7":
                self.recore.add_setting("revision", "A7")
            case "Recore A6":
                self.recore.add_setting("revision", "A6")
            case "Recore A5":
                self.recore.add_setting("revision", "A5")

        self.recore.add_setting("gain_t0", 1)
        self.recore.add_setting("gain_t1", 1)
        self.recore.add_setting("gain_t2", 1)
        self.recore.add_setting("gain_t3", 1)
        self.recore.add_setting("pullup_t0", 1)
        self.recore.add_setting("pullup_t1", 1)
        self.recore.add_setting("pullup_t2", 1)
        self.recore.add_setting("pullup_t3", 1)
        if board != "Recore A5":
            self.recore.add_setting("offset_t0", 0)
            self.recore.add_setting("offset_t1", 0)
            self.recore.add_setting("offset_t2", 0)
            self.recore.add_setting("offset_t3", 0)

        self.mcu.add_setting("serial", "/dev/ttyS4")
        self.mcu.add_setting("baud", 250000)
        self.mcu.add_setting("restart_method", "command")

        self.mcu_ar100.add_setting("serial", "/dev/ttyS1")
        self.mcu_ar100.add_setting("baud", 1500000)

    def get_recore_config(self):
        return self.recore

    def get_mcu_config(self):
        return self.mcu

    def get_mcu_ar100_config(self):
        return self.mcu_ar100
