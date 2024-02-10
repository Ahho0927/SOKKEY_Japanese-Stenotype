""""""
from pynput.keyboard import Key
from tqdm import tqdm

KEY_LOWER: str = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
KEY_UPPER: str = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
KEY_ALL: str = KEY_LOWER + KEY_UPPER

KEY_MOVE: list[Key] = [Key.up, Key.down, Key.left, Key.right, Key.home, Key.end]

KEY_USED: list[str] = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
                       'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 
                                     'c', 'v',   'n', 'm']

KEY_BLOCKED: list[str] = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 
                          'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 
                                            'c', 'v',    'n', 'm']

KEY_TRANSLATION: dict[str] = {'q': 'p', 'w': 's', 'e': 't', 'r': 'k', 't': 'h', 'y': 'u', 'u': 'a', 'i': 'o', 'o': 'i', 'p': 'e', 
                              'a': 'P', 's': 'S', 'd': 'T', 'f': 'K', 'g': 'H', 'h': 'U', 'j': 'A', 'k': 'O', 'l': 'I', ';': 'E', 
                                                 'c': 'Y', 'v': 'N',   'n': 'ん', 'm': 'っ'}

KEY_CONSONANT: list[str] = ['a', 'q', 's', 'w', 'd', 'e', 'f', 'r', 'g', 't', 'v']
KEY_VOWEL: list[str] = ['c', 'h', 'y', 'j', 'u', 'k', 'i', 'l', 'o', ';', 'p']
KEY_SPECIAL: list[str] = ['n', "m"]

CONSONANT: str = 'PpSsTtKkHhN'
VOWEL: str = 'YyUuAaOoIiEe'
SPECIAL: str = 'んっ'

CHO_TRANSLATION: dict[str] = None

key_wrote: dict[str: int] = {key: 0 for key in KEY_ALL}
key_wrote[' '] = 0

print('Loading Datas ...')

with open('./macros.txt', "r", encoding='utf-8') as f:
    datas = f.readlines()

MACRO_DATA: dict[str] = {}
for line in tqdm(datas):
    if ';' in line:
        continue

    if '||' in line:
        line = line.replace('\n', '')
        key, value = line.split('||')
        # print(line)

        consonant, vowel, special = '', '', ''
        for letter in CONSONANT:
            if letter in key:
                consonant += letter
        for letter in VOWEL:
            if letter in key:
                vowel += letter
        for letter in SPECIAL:
            if letter in key:
                special += letter

        MACRO_DATA[consonant+vowel+special] = value

# print(MACRO_DATA)
