import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import parse_qs
from wizard_db import WizardsDB

class WizardHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # Split path at '/'
        # path.split('/')

        # If-elif chain for path is called (path)routing
        if self.path == "/wizards":
            self.handleWizardList()
        elif self.path == "/wizards/someID":
            self.handle404()

        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == "/wizards":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length).decode("utf-8")
            parsed_body = parse_qs(body)

            if  'name'   not in parsed_body or \
                'age'    not in parsed_body or \
                'color'  not in parsed_body or \
                'height' not in parsed_body:
                self.send_response(422)
                self.end_headers()

            name = parsed_body['name'][0]
            age = parsed_body['age'][0]
            color = parsed_body['color'][0]
            height = parsed_body['height'][0]

            db = WizardsDB()
            db.createWizard(name, age, color, height)

            self.send_response(201)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes("Created", "utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def handleWizardList(self):
        db = WizardsDB()

        wizards = db.getWizards()

        json_string = json.dumps(wizards)
        print("JSON String: {0}".format(json_string))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(bytes(json_string, "utf-8"))

    def handle404(self):
        self.send_response(404)
        self.end_headers()

def main():
    listen = ("0.0.0.0", 8080)
    server = HTTPServer(listen, WizardHTTPRequestHandler)

    print("Starting server..")
    server.serve_forever()

main()
