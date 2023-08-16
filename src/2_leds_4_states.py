from machine import Pin
from utime import sleep_ms

# Read the button's state, either pressed or unpressed, for every this value of ms.
BUTTON_STATUS_READ_PERIOD = 250

# Set pull = Pin.PULL_DOWN so that Pico sees a low level (button.value() = 0)
# when the button is not pressed.
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

onboard_led = Pin("LED", Pin.OUT, value=0)
external_led = Pin(15, Pin.OUT, value=0)

# Default state (b00): both the LEDs are off.
# First press (b01): turn on the onboard LED.
# Second press (b10): turn on the external LED and turn off the onboard LED.
# Third press (b11): turn on both the LEDs.
leds_current_state = 0
while True:
    if button.value() == 0:
        continue

    leds_current_state += button.value()
    leds_current_state %= 4

    if leds_current_state == 1:
        onboard_led.value(1)

    elif leds_current_state == 2:
        onboard_led.value(0)
        external_led.value(1)

    elif leds_current_state == 3:
        onboard_led.value(1)
        external_led.value(1)

    else:
        onboard_led.value(0)
        external_led.value(0)

    sleep_ms(button.value() * BUTTON_STATUS_READ_PERIOD)
