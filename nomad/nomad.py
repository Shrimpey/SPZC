from django.core.handlers.wsgi import WSGIRequest

from nomad.tagger import Tagger


class NomadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.tagger = Tagger(parameter_tag='__RaNmE__')

    def __call__(self, request: WSGIRequest):
        print(request.session.session_key)  # DEBUG
        print(request.method == 'GET')
        print(self.get_client_ip(request))
        if not request.session.exists(request.session.session_key):
            request.session.create()

        response = self.get_response(request)

        if request.method == "GET":
            response.content = self.tagger.randomize_elements(html_doc=response.content,
                                                              session_id=request.session.session_key,
                                                              client_id=self.get_client_ip(request))
        elif request.method in ['POST', 'PUT']:
            pass  # TODO Trzeba zamienić że przecież w poscie nie idzie html tylko json, czy coś innego
            # Może coś takiego, że derandomizujemy htmla i tworzymy słownik {randomizowane_id : id}
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
