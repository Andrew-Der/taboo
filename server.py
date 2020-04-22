import os

from http.server import BaseHTTPRequestHandler

# from http_response.staticHandler import StaticHandler
from http_response.template_handler import TemplateHandler
from http_response.bad_request_handler import BadRequestHandler
from http_response.no_action_handler import NoActionHandler

from game_logic import start_game
from game_logic import init_game

routes = {
    "/" : {
        "template" : "index.html" 
    },
    "/start" : {
        "template" : "start.html"
    }, 
    "/start-game" : {},
    "/init-game" : {},
    "/fetch-cards" : {},
    "/update-score" : {},

}


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]
        handler = NoActionHandler()

        if self.path in routes:
            if self.path == "/init-game":
                if init_game(self):
                    handler = NoActionHandler()
                else:
                    handler = BadRequestHandler()
        else:
            handler = BadRequestHandler()
    
        self.respond({
            'handler': handler 
        })

    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"

        self.end_headers()

        if isinstance(content, bytes):
            return content
        else:
            return bytes(content, 'UTF-8')
            
    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)