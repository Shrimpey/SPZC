import re

import schedule
import hashlib
import base64

from Crypto import Random
from Crypto.Cipher import AES


SEED = 69


def xor_shift():
    global SEED
    for i in range(10):
        SEED = (SEED * 1664525 + 1013904223) & 0xFFFFFFFF
    return SEED


class AESCipher:
    def __init__(self, byte_key):
        self.block_size = AES.block_size
        self.key = byte_key

    def encrypt(self, plain_text):
        plain_text = self._pad(plain_text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(plain_text.encode()))

    def decrypt(self, encrypted_text):
        # some magic from SO
        altchars = b'+/'
        encrypted_text = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', encrypted_text)
        missing_padding = len(encrypted_text) % 4
        if missing_padding:
            encrypted_text += b'=' * (4 - missing_padding)

        encrypted_text = base64.b64decode(encrypted_text, altchars)
        iv = encrypted_text[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(encrypted_text[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * \
               chr(self.block_size - len(s) % self.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class Randomizer:
    def __init__(self, time_slot_len: int = 30, hashing_func: str = 'sha256'):
        self._hashing_func = hashing_func

        self._current_master_key = self._gen_master_key()
        schedule.every(time_slot_len).minutes.do(self._gen_master_key)

        self._session_master_dict = {}  # {session_id : master_key}
        schedule.every(time_slot_len).minutes.do(self._update_session_key_dict)

    @staticmethod
    def _gen_master_key():
        return xor_shift()

    def _add_new_connection(self, session_id):
        self._session_master_dict[session_id] = self._current_master_key

    def _update_session_key_dict(self):  # TODO
        """
         checks if there are session ids in keys that are no longer valid
        """
        pass

    def _get_session_key(self, session_id, client_id):
        hash_container = hashlib.new(name=self._hashing_func)
        if session_id not in self._session_master_dict.keys():
            self._add_new_connection(session_id)
        master_key = self._session_master_dict[session_id]

        hash_container.update(str(master_key).encode('UTF-8'))
        hash_container.update(str(client_id).encode('UTF-8'))
        return hash_container.digest()

    def randomize_parameter(self, param_value, session_id, client_id):
        session_key = self._get_session_key(session_id, client_id)
        aes = AESCipher(byte_key=session_key)
        return aes.encrypt(param_value).decode('UTF-8')

    def derandomize_parameter(self, randomized_value, session_id, client_id):
        randomized_value = randomized_value.encode('UTF-8')
        session_key = self._get_session_key(session_id, client_id)
        aes = AESCipher(byte_key=session_key)
        return aes.decrypt(randomized_value)


if __name__ == '__main__':
    session = 'abc'
    client = 'twuj stary'
    parameter = 'bruhhhhhh'
    print(f'ORINAL KEY: {parameter}')
    r = Randomizer(time_slot_len=1)
    randomized = r.randomize_parameter(param_value=parameter, session_id=session, client_id=client)
    print(f'RANDOMIZED: {randomized}')
    derandomized = r.derandomize_parameter(randomized_value=randomized, session_id=session, client_id=client)
    print(f'DERANDOMIZED: {derandomized}')

