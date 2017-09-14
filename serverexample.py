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


        print("GET PATH: ", self.path)

        if self.path == "/pandas":
            self.send_header("Content-Type", "text/html") # "text/html" is a MIME type
            self.end_headers() # Tell python when your done with headers, even if there aren't any
            self.wfile.write(bytes("<strong>PANDAS!!</strong>", "utf-8"))

        elif self.path == "/potatoes":
            self.send_header("Content-Type", "text/html") # "text/html" is a MIME type
            self.end_headers() # Tell python when your done with headers, even if there aren't any
            self.wfile.write(bytes("<strong>POTATOES!!</strong>", "utf-8"))

        else:
            self.send_header("Content-Type", "text/html") # "text/html" is a MIME type
            self.end_headers() # Tell python when your done with headers, even if there aren't any
            self.wfile.write(bytes("<strong>Hello<strong>", "utf-8")) # Create body (Text, character set)

        # self.wfile is a file object. Not writing to a file, but the buffering benefits
        # of a file object can be applied here. Response body

        #self.path to access path string

    def do_POST(self):
        print("POST PATH: ", self.path)

        if self.path == "/potatoes":
            length = self.headers["Content-Length"] # Number of bytes inside body of request
            length = int(length) # length is originally a string
            print("Content-Length: ", length)

            body = self.rfile.read(length).decode("utf-8")
            print("REQUEST BODY: ", body)
            # parse_qs() import from a module
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<strong>POST DONE</strong>", "utf-8"))

def main():
    listen = ("0.0.0.0", 8080) # (Host, Port)
    server = HTTPServer(listen, MyHandler) # Instantiate the server

    print("Listening...") # Print before serve_forever to know it is working
    server.serve_forever() # Will not return

main()
