from simpili.gpio_internal_state import GPIOInternalState

class SimGPIO:
    """
    Simulates the RPi.GPIO library by relaying state through a SimServer.
    """
    BCM = 11
    BOARD = 10
    MODE_UNKNOWN = -1
    SERIAL = 40
    SPI = 41
    I2C = 42
    PWM = 43
    HIGH = 1
    LOW = 0
    INPUT = 1
    OUTPUT = 0
    PUD_OFF = 0
    PUD_DOWN = 1
    PUD_UP = 2

    # TODO: Validate pin usages

    _internal_state = GPIOInternalState()

    @staticmethod
    def setmode(mode):
        SimGPIO._internal_state.mode = mode
        SimGPIO._internal_state.update()

    @staticmethod
    def setup(pin, mode, pud=PUD_OFF):
        SimGPIO._internal_state.pin_setups[pin] = (mode, pud)
        SimGPIO._internal_state.update()

    @staticmethod
    def write(pin, value):
        mode, pud = SimGPIO._internal_state.pin_setups[pin]
        if mode == SimGPIO.INPUT:
            return

        SimGPIO._internal_state.pin_values[pin] = \
            SimGPIO.HIGH if value else SimGPIO.LOW
        SimGPIO._internal_state.update()

    def read(pin):
        return SimGPIO._internal_state.pin_values[pin]