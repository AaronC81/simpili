from simpili.sim_server import SimServer
import json

class GPIOInternalState:
    """
    Stores hidden internal GPIO simulation state.
    """

    def __init__(self):
        if SimServer._state is not None:
            print("### WARNING: Overwriting the SimServer state.")
        SimServer._state = self
        self.mode = None
        self.pin_setups = {}
        self.pin_values = {}

    def update(self):
        SimServer.update()        

    def json(self):
        return json.dumps({
            "mode": self.mode,
            "pin_setups": self.pin_setups,
            "pin_values": self.pin_values
        })