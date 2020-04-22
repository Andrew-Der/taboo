from http_response.request_handler import RequestHandler

class BadRequestHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/plain'
        self.setStatus(404)