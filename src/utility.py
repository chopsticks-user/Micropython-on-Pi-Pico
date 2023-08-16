from machine import ADC

def get_board_temperature(unit = 'C'):
    current_temp = 27 - (ADC(4).read_u16() * 3.3 / 65535 - 0.706) / 0.001721   
    if unit == 'F':
        return current_temp * 1.8 + 32
    if unit == 'K':
        return current_temp + 273.15
    return current_temp