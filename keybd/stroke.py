"""pynput and keyboard helps approach to keyboard or mouse easily.
"""
from pynput.keyboard import Key, Controller
from keybd.keys import KEY_USED, key_wrote
from keybd.translate import Translate
from keybd.key_control import KeyControl
translate = Translate()
key_control = KeyControl()

class Stroke:
    """Class about Key Stroke.
    """
    def __init__(self) -> None:
        self.key_monitor = set()
        self.key_in_stroke = set()

    def on_press(self, key) -> None:
        """This get physically pressed keys sent from Listener() in main.py.
        If self.key_monitor was empty before this function runs, the stroke starts.

        Args:
            key (Key): the pressed key.
        """
        try:
            key = key.char
        except AttributeError:
            pass

        if key in KEY_USED:
            if key_wrote[key] == 0:
                self.key_monitor.add(key)
                self.key_in_stroke.add(key)
            else:
                key_wrote[key] -= 1
        else:
            if key == Key.esc:
                return False
            elif key == ']':
                Controller().press(Key.ctrl_l)
                Controller().press(Key.backspace)
                Controller().release(Key.backspace)
                Controller().release(Key.ctrl_l)

    def on_release(self, key) -> None:
        """This get physically released keys sent from Listener() in main.py.
        If self.key_monitor is empty after this function ran, the stroke ends.

        Args:
            key (Key): the released key.
        """
        try:
            key = key.char
        except AttributeError:
            pass

        if key in KEY_USED:
            try:
                self.key_monitor.remove(key)

                if len(self.key_monitor) == 0:
                    print(self.key_in_stroke)

                    result = translate.get_result(self.key_in_stroke)
                    print('"'+result+'"')

                    key_control.send_inputs(result)

                    # RESET
                    self.key_in_stroke = set()
                    print()

            except KeyError:
                pass
