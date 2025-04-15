# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import KeysScanner, DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    row_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP26, board.GP27),
    col_pins=(board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22),
    diode_orientation=DiodeOrientation.COL2ROW,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        # Row 1: F-keys (optional if you wire them)
        [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.SLCK]

        # Row 2
        [KC.GRV, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7, KC._8, KC._9, KC._0, KC.MINS, KC.EQUAL, KC.BSPC, KC.NO]

        # Row 3
        [KC.TAB, KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS]

        # Row 4
        [KC.CAPS, KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO]

        # Row 5
        [KC.LSFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.NO, KC.UP]

        # Row 6 (Bottom row)
        [KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN]

        # Row 7 (Not Physical)
        [KC.INS, KC.CALC, KC.PGUP, KC.SCRL, KC.PSLS, KC.PAST, KC.PMNS, KC.P7, KC.P8, KC.P9, KC.PPLS, KC.P4, KC.P5, KC.P6]

        # Row 7 (Not Physical)
        [KC.LEFT, KC.P1, KC.P2, KC.P3, KC.PENT, KC.P0, KC.PDOT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()