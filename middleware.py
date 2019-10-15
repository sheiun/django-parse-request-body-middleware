from .util import RequestBodyDecoder


class RequsetBodyParseMiddleware:
    """Requset Body Parse Middleware"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.data = RequestBodyDecoder(request.body, request.POST).decode()
        response = self.get_response(request)
        return response