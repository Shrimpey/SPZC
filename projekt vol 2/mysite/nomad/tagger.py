from typing import List
from bs4 import BeautifulSoup

from nomad.randomizer import Randomizer


class Tagger:
    def __init__(self, parameter_tag: str, special_attr_name: str = 'nomad'):
        self._parameter_tag = parameter_tag
        self._special_attr = special_attr_name
        self._randomizer = Randomizer()

    # TODO session_id ma być zbierane z django a client_id to ma być IP kolesia
    def randomize_elements(self, html_doc: str) -> str:
        """
        :param html_doc: HTML document where attributes
        that have to be randomized are tagged with a special tag

        :return: an HTML document with randomized values
        and special attributes informing about randomization
        """
        soup = BeautifulSoup(html_doc, 'html.parser')
        tagged_elements = self._get_tagged_elements(soup)
        for e in tagged_elements:
            for tag in soup.find_all(attrs={e[0]: e[1]}):
                tag[self._special_attr] = e[0]
                tag[e[0]] = self._randomizer.randomize_parameter(param_value=e[1],
                                                                 session_id='TODO',
                                                                 client_id='TODO')
        return str(soup)

    # TODO session_id ma być zbierane z django a client_id to ma być IP kolesia
    def derandomize_elements(self, html_doc: str) -> str:
        """
        :param html_doc: HTML document where attributes special attributes
        :return: an HTML document with derandomized values
        """
        soup = BeautifulSoup(html_doc, 'html.parser')
        randomized_elements = self._get_randomized_elements(soup)
        for e in randomized_elements:
            for tag in soup.find(attrs={e[0]: e[1]}):
                tag[self._special_attr] = e[0]
                tag[e[0]] = self._randomizer.derandomize_parameter(randomized_value=e[1],
                                                                   session_id='TODO',
                                                                   client_id='TODO')
        return str(soup)

    def _get_tagged_elements(self, soup: BeautifulSoup) -> List[(str, str)]:
        elements = []
        for e in soup():
            for attr_name, value in e.attrs.items():
                if type(value) == str and value.startswith(self._parameter_tag):
                    elements.append((attr_name, value))
        return list(set(elements))

    def _get_randomized_elements(self, soup: BeautifulSoup) -> List[(str, str)]:
        """
        This method finds all html elements with a special attribute
        If found, checks the value of said attr. This value describes a name of a randomized attribute.
        Ex. let's say that special attr is called "nomad". Then <p nomad="id" id="sXcdjnArrA!2SS"> will be picked
        :return: List of tuples, where tuple[0] - randomized attr name, tuple[1] - randomized attr value
        """
        elements = soup.find_all(attrs={self._special_attr: True})
        return [(e[self._special_attr], e[e[self._special_attr]]) for e in elements]
