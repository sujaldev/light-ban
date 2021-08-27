from tuyapy.tuyaapi import TuyaApi
from time import sleep


# noinspection PyMethodMayBeStatic
class Controller:
    def __init__(self, username, password, country_code, biz_type=""):
        self.username = username
        self.password = password
        self.country_code = country_code
        self.biz_type = biz_type

        self.api = TuyaApi()
        self.api.init(username, password, country_code, biz_type)
        self.lights = [device for device in self.api.get_all_devices() if device.device_type() == "light"]

        self.ban_enabled = False

    def change_lights_to_tolerable_mode(self):
        for light in self.lights:
            light.turn_on()
            light.set_brightness(1000)
            light.set_color([0, 0, 100])
            light.set_color_temp(36294)

    def enable_ban(self):
        while self.ban_enabled:
            self.change_lights_to_tolerable_mode()
            sleep(10)
