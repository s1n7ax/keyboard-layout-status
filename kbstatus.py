import sys
import re


from typing import List

class KeyPosition:
    def __init__(self, top = False, right = False, bottom = False, left = False):
        self.top: bool = top
        self.right: bool = right
        self.bottom: bool = bottom
        self.left: bool = left


class Key:
    def __init__(self, value: str, finger: int, pos: str):
        self.value = value
        self.finger = finger
        self.pos = pos

    def has_movement(self) -> bool:
        return self.pos != 'none'

    def __str__(self) -> str:
        return 'value="{0}" finger="{1}" pos="{2}"'.format(self.value,
                self.finger, self.pos)


class KeyboardBuilder:
    def build(self, key_layout) -> dict[str, Key]:
        keys: dict[str, Key] = {}

        for y, row in enumerate(key_layout):
            for x, key in enumerate(row):
                key_obj = Key(key, self.get_finger_from_row(x),
                        self.get_key_position(x, y))
                keys[key] = key_obj

        return keys

    def get_finger_from_row(self, y: int) -> int:
        if y < 4:
            return y

        if y == 4:
            return 3

        if y == 5:
            return 4

        return y - 1

    def get_key_position(self, x: int, y: int) -> str:
        top = False
        bottom = False
        right = False
        left = False

        if y == 0:
             top = True

        if y == 2:
             bottom = True

        if x == 4:
             right = True

        if x == 5:
            left = True

        if top:
            if right:
                return 'top right'
            if left:
                return 'top left'
            return 'top'

        if bottom:
            if right:
                return 'bottom right'
            if left:
                return 'bottom left'
            return 'bottom'

        if right:
            return 'right'

        if left:
            return 'left'

        return 'none'


class KeyboardFactory:

    @staticmethod
    def get_layout(layout) -> dict[str, Key]:

        if layout == 'qwerty':
            return KeyboardBuilder().build([
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
            ])

        if layout == 'dvorak':
            return KeyboardBuilder().build([
                ["'", ",", ".", "p", "y", "f", "g", "c", "r", "l"],
                ["a", "o", "e", "u", "i", "d", "h", "t", "n", "s"],
                [";", "q", "j", "k", "x", "b", "m", "w", "v", "z"]
            ])

        if layout == 'colemak':
            return KeyboardBuilder().build([
                ["q", "w", "f", "p", "g", "j", "l", "u", "y", ";"],
                ["a", "r", "s", "t", "d", "h", "n", "e", "i", "o"],
                ["z", "x", "c", "v", "b", "k", "m", ",", ".", "/"]
            ])

        if layout == 'workman':
            return KeyboardBuilder().build([
                ["q", "d", "r", "w", "b", "j", "f", "u", "p", ";"],
                ["a", "s", "h", "t", "g", "y", "n", "e", "o", "i"],
                ["z", "x", "m", "c", "v", "k", "l", ",", ".", "/"]
            ])

        raise Exception("unknown keyboard layout")


class StatusReport:
    def __init__(self, name, keyboard: dict[str, Key]):
        self.name = name
        self.keyboard = keyboard

        self.row_format ="{:<20}" * 2

        self.prev_finger = None
        self.prev_char = None

        self.finger_movement_count = 0
        self.same_finger_use = 0
        self.moves = {
                'none': 0,
                'top': 0,
                'bottom': 0,
                'left': 0,
                'right': 0,
                'top right': 0,
                'top left': 0,
                'bottom right': 0,
                'bottom left': 0,
        }

    def calculate(self, value: str):
        value = re.sub(r"[^a-zA-Z]*", "", value)

        for char in value:
            key = self.keyboard[char.lower()]

            self.moves[key.pos] = self.moves[key.pos] + 1

            if key.has_movement():
                self.finger_movement_count = self.finger_movement_count + 1

            if self.prev_char != key.value and self.prev_finger == key.finger:
                self.same_finger_use = self.same_finger_use + 1

            self.prev_finger = key.finger
            self.prev_char = key.value

    def print_status(self):
        print()
        print('-------------{0}-------------'.format(self.name))
        print(self.row_format.format('No Movements', self.moves['none']))
        print(self.row_format.format('Finger Movements', self.finger_movement_count))
        print(self.row_format.format('Same Finger Use', self.same_finger_use))

        print(self.row_format.format('Up',self.moves['top']))
        print(self.row_format.format('Down',self.moves['bottom']))
        print(self.row_format.format('Left',self.moves['left']))
        print(self.row_format.format('Right',self.moves['right']))
        
        print(self.row_format.format('Top Right',self.moves['top right']))
        print(self.row_format.format('Top Left',self.moves['top left']))
        print(self.row_format.format('Bottom Right ',self.moves['bottom right']))
        print(self.row_format.format('Bottom Left',self.moves['bottom left']))



def main():

    layouts: List[StatusReport] = [
        StatusReport('QWERTY', KeyboardFactory.get_layout('qwerty')),
        StatusReport('DVORAK', KeyboardFactory.get_layout('dvorak')),
        StatusReport('WORKMAN', KeyboardFactory.get_layout('workman')),
        StatusReport('COLEMAK', KeyboardFactory.get_layout('colemak')),
    ]

    for line in sys.stdin:
        for layout in layouts:
            layout.calculate(line)

    for layout in layouts:
        layout.print_status()

if __name__ == '__main__':
    main()
