import struct
import subprocess

import pwnagotchi
import pwnagotchi.plugins as plugins
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK

# ADDRESS = int(''.join(filter(str.isdigit, str(subprocess.run(["sudo", "i2cdetect", "-y", "1"], capture_output=True)).split("70:")[1])), 16)
ADDRESS = 0x76


class UPS:
    def __init__(self):
        import smbus2

        self._bus = smbus2.SMBus(1)

    def readVoltage(self):
        try:
            read = self._bus.read_word_data(ADDRESS, 2) # or input i2c = 2(default ups), 21, 12(test), 9
            # logging.info("voltage read: " + str(read))
            swapped = struct.unpack("<H", struct.pack(">H", read))[0]
            # logging.info("voltage swapped: " + str(swapped))
            voltage = swapped * 1.25 / 1000 / 16
            # logging.info("voltage return: " + str(voltage))

            return voltage
        except:
            return 0.0

    def readCapacity(self):
        try:
            read = self._bus.read_word_data(ADDRESS, 21)  # or i2c = 2(test), 4(default ups 1.1)
            # logging.info("capacity read: " + str(read))
            swapped = struct.unpack("<H", struct.pack(">H", read))[0]
            # logging.info("capacity swapped: " + str(swapped))
            capacity = swapped / 256
            # logging.info("capacity return: " + str(capacity))

            return capacity
        except:
            return 0.0

    def quickStart(self):
        self._bus.write_word_data(ADDRESS, 0x06, 0x4000)


class UPSLite(plugins.Plugin):
    __author__ = 'Egor Levashov (sxfour)'
    __version__ = '0.0.4'
    __license__ = 'GPL3'
    __description__ = '(TEST) A plugin that will add a voltage indicator for the UPS Lite v1.0'

    def __init__(self):
        self.ups = None

    def on_loaded(self):
        self.ups = UPS()

    def on_ui_setup(self, ui):
        ui.add_element('ups', LabeledValue(color=BLACK, label='', value='0mA/0Вт', position=(ui.width() / 3, 0),
                                           label_font=fonts.Bold, text_font=fonts.Medium))

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element('ups')

    def on_ui_update(self, ui):
        self.ups.quickStart()
        voltage = self.ups.readVoltage()
        capacity = self.ups.readCapacity()
        # ui.set('ups', "%5imA/%5.2fВт" % (capacity, voltage))
        if voltage >= 0.97:
            ui.set('ups', "%5imA/%5.2fВт" % (capacity, voltage))
        elif voltage <= 0.96:
            ui.set('ups', "выключен")
            ui.update(force=True, new_data={'status': 'Низкий заряд, поки-доки...'})
            pwnagotchi.shutdown()
        else:
            ui.set('ups', "ошибка...")
