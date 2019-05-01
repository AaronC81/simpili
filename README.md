# SimPiLi
SimPiLi (pronounced _simply_) is the **Sim**ulator for **Pi** **Lib**rary. It
simulates the core elements of the Raspberry Pi's `RPi.GPIO` library, acting
effectively as a virtual Pi.

The current Pi state is broadcasted to local clients through a WebSocket, 
allowing clients to be modular and indepedent of SimPiLi.

## How do I use it?
In most cases, all you need to do is replace `import RPi.GPIO as GPIO` with
`from simpili import GPIO`:

```python
from simpili import GPIO # <-- !!!
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUTPUT)

while True:
    GPIO.write(13, GPIO.HIGH)
    sleep(1)
    GPIO.write(13, GPIO.LOW)
    sleep(1)
```

## How does it work?
SimPiLi attempts to import `RPi.GPIO`. If this succeeds (i.e. you're using a
hardware Raspberry Pi), then `SimPiLi.GPIO` simply aliases `RPi.GPIO` and the
real GPIO is used.

If this import fails, the simulator starts. `SimPiLi.GPIO` is set to 
`SimPiLi.SimGPIO` and a WebSocket server is started. The `SimGPIO` class aims
to simulate the behaviour of the authentic `RPi.GPIO` class as much as possible.

Whenever state changes, the new state is broadcast as JSON to all WebSocket 
clients connected on port 52774.