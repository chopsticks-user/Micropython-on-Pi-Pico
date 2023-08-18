from machine import ADC, Pin, Timer
import network


def periodically_blink_ob_led(time_interval=1000):
    def tick(timer):
        global _ob_led
        _ob_led = Pin("LED", Pin.OUT)
        _ob_led.toggle()

    timer = Timer()
    timer.init(freq=1000/time_interval, mode=Timer.PERIODIC, callback=tick)


def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)


def get_board_temperature(unit='C'):
    current_temp = 27 - (ADC(4).read_u16() * 3.3 / 65535 - 0.706) / 0.001721
    if unit == 'F':
        return current_temp * 1.8 + 32
    if unit == 'K':
        return current_temp + 273.15
    return current_temp
