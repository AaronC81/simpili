from simpili.sim_gpio import SimGPIO
from simpili.sim_server import SimServer

try:
    GPIO = __import__("RPi").GPIO
except ModuleNotFoundError:
    GPIO = SimGPIO
    SimServer.start()