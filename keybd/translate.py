"""hgtk supports variable functions about Hangul.
"""
from keybd.keys import KEY_TRANSLATION, KEY_CONSONANT, KEY_VOWEL, KEY_SPECIAL, MACRO_DATA
from keybd.key_control import KeyControl
key_control = KeyControl()

class NoCombinableResult(Exception):
    """Custom Exception which rises when the result from macros 
    don't have '-'(i.e. literally not an combinable result).
    """
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        # self.errors = errors

class Translate:
    """Translater into Hangul result from pressed keys.
    """
    def __init__(self) -> None:
        self.previous_result = '가'

    def get_result(self, keys: set) -> str:
        """get result made of hangul or symbols from pressed_keys(keys)

        Args:
            keys (set): previously pressed keys

        Raises:
            Exception: KeyError, NotHangulException, etc.

        Returns:
            str: the result made of hangul or symbols
        """
        consonant, vowel, special = self._key_analyzer(keys)
        indicator = consonant + vowel + special
        print(indicator)

        result = ''
        try:
            result = MACRO_DATA[indicator]
        except KeyError:
            pass

        self.previous_result += result
        if len(self.previous_result) > 10:
            self.previous_result = self.previous_result[2:]

        return result

    def _key_analyzer(self, keys: set):

        consonant, vowel, special = '', '', ''
        for key in KEY_CONSONANT:
            if key in keys:
                consonant += KEY_TRANSLATION.get(key, '')
        for key in KEY_VOWEL:
            if key in keys:
                vowel += KEY_TRANSLATION.get(key, '')
        for key in KEY_SPECIAL:
            if key in keys:
                special += KEY_TRANSLATION.get(key, '')

        return consonant, vowel, special
