from http_response.request_handler import RequestHandler

class NoActionHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'
        self.contents = open('templates/dummy.html') 
        self.setStatus(200)