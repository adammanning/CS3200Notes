from http.server import BaseHTTPRequestHandler, HTTPServer # Importing two classes from module http.server

# Create subclass of BaseHTTPRequestHandler
# Will be instantiated with EVERY request and then dies after response is given
class MyHandler(BaseHTTPRequestHandler):
    pass

def main():
    listen = ("127.0.0.1", 8080) # (Host, Port)
    server = HTTPServer(listen, MyHandler) # Instantiate the server

    print("Listening...") # Print before serve_forever to know it is working
    server.serve_forever() # Will not return

main()
