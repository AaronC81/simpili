import websockets
import asyncio
from threading import Thread

class SimServer:
    """
    A WebSocket server which sends server state to clients whenever it changes.
    """

    _state = None
    _update_required = False
    _websockets = []

    @staticmethod
    async def server_loop(websocket, _):
        """
        An async server loop.
        """
        # Forever wait for update to be required
        print("### Connection opened.")
        try:
            SimServer._websockets.append(websocket)
            while True:
                pass
        finally:
            SimServer._websockets.remove(websocket)
            
    @staticmethod
    def update():
        """
        Sends a simulation server update to all WebSockets.
        """
        print("### Updating...")

        # TODO: remove closed sockets
        for socket in SimServer._websockets:
            asyncio.get_event_loop().run_until_complete(socket.send(SimServer._state.json()))

    @staticmethod
    def start(port=52774):
        """
        Begins the server.
        """
        print("### Starting SimPiLi server on port " + str(port) + "...")

        def thread():
            loop = asyncio.new_event_loop()
            server = websockets.serve(SimServer.server_loop, "localhost", port, loop=loop)
            loop.run_until_complete(server)
            loop.run_forever()

        Thread(target=thread).start()
        
        print("### SimPiLi server started.")
