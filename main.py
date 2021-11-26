#import asyncio
from socketserver import TCPServer, StreamRequestHandler

class RequestHandler(StreamRequestHandler):
    """The request handler class for the server

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def setup(self):
        print("Entered setup...")

    def handle(self):
        print("Handling request...")
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        self.request.sendall(data.upper())

    def finish(self):
        print("Entered finish...")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8080

    # Create the server, binding to localhost on port 80
    with TCPServer((HOST, PORT), RequestHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()