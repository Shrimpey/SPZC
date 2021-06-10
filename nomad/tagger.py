from typing import List
from bs4 import BeautifulSoup
from django.http import QueryDict

from nomad.randomizer import Randomizer


class Tagger:
    _params_to_randomize = {}   # private dict where key: parameter type (like name) and
                                # value is a list of parameter values (like "id1", "submit_btn" etc)

    @staticmethod
    def add_param_to_randomize(param_types: List[str], value: str):
        for param_type in param_types:
            if param_type not in Tagger._params_to_randomize.keys():
                Tagger._params_to_randomize[param_type] = [value]
            else:
                Tagger._params_to_randomize[param_type].append(value)

    def __init__(self):
        self._randomizer = Randomizer()


    def randomize_elements(self, html_doc: str, session_id: str, client_id: str) -> str:
        """
        :param session_id: current session key
        :param client_id: client's IP address
        :param html_doc: HTML document where attributes
        that have to be randomized are tagged with a special tag

        :return: an HTML document with randomized values
        and special attributes informing about randomization
        """
        soup = BeautifulSoup(html_doc, 'html.parser')
        tagged_elements = self._get_tagged_elements(soup)
        for e in tagged_elements:
            for tag in soup.find_all(attrs={e[0]: e[1]}):
                tag[e[0]] = self._randomizer.randomize_parameter(param_value=e[1],
                                                                 session_id=session_id,
                                                                 client_id=client_id)
        return str(soup)

    def derandomize_elements(self, request_form: QueryDict, session_id: str, client_id: str) -> None:
        if not request_form._mutable:
            request_form._mutable = True

        for key, value in request_form.copy().items():
            # check for base64
            if len(key.strip()) % 4 == 0:
                try:
                    derandomized_key = self._randomizer.derandomize_parameter(key,
                                                                              session_id=session_id,
                                                                              client_id=client_id)
                    request_form[derandomized_key] = value
                except ValueError:
                    print("Got invalid value on request")

    def _get_tagged_elements(self, soup: BeautifulSoup):
        elements = []
        for e in soup():
            for attr_name, value in e.attrs.items():
                if attr_name in self._params_to_randomize.keys() \
                        and value in self._params_to_randomize[attr_name]:
                    elements.append((attr_name, value))
        return list(set(elements))
