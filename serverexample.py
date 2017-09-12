from http.server import BaseHTTPRequestHandler, HTTPServer # Importing two classes from module http.server

# Create subclass of BaseHTTPRequestHandler
# Will be instantiated with EVERY request and then dies after response is given

# Always in this order
# 1 Send response
# 2 Any headers
# 3 End headers
# 4 Wirte the body

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # Actually sends the request status
        self.send_header("Content-Type", "text/html") # "text/html" is a MIME type
        self.end_headers() # Tell python when your done with headers, even if there aren't any
        self.wfile.write(bytes("<strong>Hello<strong>", "utf-8")) # Create body (Text, character set)
        # self.wfile is a file object. Not writing to a file, but the buffering benefits
        # of a file object can be applied here. Response body

        #self.path to access path string

def main():
    listen = ("127.0.0.1", 8080) # (Host, Port)
    server = HTTPServer(listen, MyHandler) # Instantiate the server

    print("Listening...") # Print before serve_forever to know it is working
    server.serve_forever() # Will not return

main()
