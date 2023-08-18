from machine import Pin
from utime import sleep
import _thread

GREEN_TIME = 10
AMBER_TIME = 3
RED_TIME = 10


def signal_handler(signal, time):
    signal.on()
    sleep(time)
    signal.off()


global crossing_allowed
crossing_allowed = False


def puffin_crossing_thread(
        button, buzzer, crossing_allowed_time):
    global crossing_allowed
    button_pressed = False
    while True:
        if button.value() == 1:
            button_pressed = True
        if crossing_allowed:
            if button_pressed:
                while crossing_allowed:
                    buzzer.on()
                    sleep(0.1)
                    buzzer.off()
                    sleep(1.9)
            else:
                sleep(crossing_allowed_time)
            button_pressed = False


led_green = Pin(13, Pin.OUT)
led_amber = Pin(14, Pin.OUT)
led_red = Pin(15, Pin.OUT)

button = Pin(9, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(12, Pin.OUT)
crossing_green_light = Pin("LED", Pin.OUT)

_thread.start_new_thread(puffin_crossing_thread,
                         (button, buzzer, RED_TIME))

while True:
    crossing_allowed = True
    crossing_green_light.on()
    signal_handler(led_red, RED_TIME)
    crossing_green_light.off()
    crossing_allowed = False

    signal_handler(led_green, GREEN_TIME)
    signal_handler(led_amber, AMBER_TIME)
