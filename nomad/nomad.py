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
        if not request.session.exists(request.session.session_key):
            request.session.create()

        if request.method == "GET":
            response = self.get_response(request)
            response.content = self.tagger.randomize_elements(html_doc=response.content,
                                                              session_id=request.session.session_key,
                                                              client_id=self.get_client_ip(request))

        if request.method in ['POST', 'PUT']:
            self.tagger.derandomize_elements(request_form=request.POST,
                                             session_id=request.session.session_key,
                                             client_id=self.get_client_ip(request))

            response = self.get_response(request)
            response.content = self.tagger.randomize_elements(html_doc=response.content,
                                                              session_id=request.session.session_key,
                                                              client_id=self.get_client_ip(request))

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
