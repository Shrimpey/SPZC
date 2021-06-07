from typing import List
from bs4 import BeautifulSoup
from django.http import QueryDict

from nomad.randomizer import Randomizer


class Tagger:
    def __init__(self, parameter_tag: str):
        self._parameter_tag = parameter_tag
        self._randomizer = Randomizer()

    # TODO session_id ma być zbierane z django a client_id to ma być IP kolesia
    def randomize_elements(self, html_doc: str, session_id: str, client_id: str) -> str:
        """
        :param session_id:
        :param client_id:
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
                derandomized_key = self._randomizer.derandomize_parameter(key,
                                                                          session_id=session_id,
                                                                          client_id=client_id)
                request_form[derandomized_key] = value

    def _get_tagged_elements(self, soup: BeautifulSoup):
        elements = []
        for e in soup():
            for attr_name, value in e.attrs.items():
                if type(value) == str and value.startswith(self._parameter_tag):
                    elements.append((attr_name, value))
        return list(set(elements))


