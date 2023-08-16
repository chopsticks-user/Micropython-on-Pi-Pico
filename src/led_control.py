from machine import Pin, Timer

def _tick(timer):
    global _ob_led
    _ob_led = Pin("LED", Pin.OUT)
    _ob_led.toggle()

def periodically_blink_ob_led(time_interval = 1000):
    timer = Timer()
    timer.init(freq=1000/time_interval, mode=Timer.PERIODIC, callback=_tick)