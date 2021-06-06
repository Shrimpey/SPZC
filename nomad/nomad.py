from django.core.handlers.wsgi import WSGIRequest
from nomad.tagger import Tagger

# ---   Time measurement related    ---
from timeit import default_timer as timer
measure_time = True
# --- End time measurement related  ---


class NomadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.tagger = Tagger(parameter_tag='__RaNmE__')

    def __call__(self, request: WSGIRequest):
        # ---   Time measurement related    ---
        if measure_time:
            starttime = timer()
        # --- End time measurement related  ---
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

        # ---   Time measurement related    ---
        if measure_time:
            print("Time taken for Nomad call:", str((timer() - starttime)*1000) + " ms")
        # --- End time measurement related  ---
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
