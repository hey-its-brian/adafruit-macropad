# Brian Meyer 2025
# This is designed to be used with the Mac version of No Man's Sky via Steam

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {
    'name' : 'NMS              ',
    'macros' : [
        # COLOR     LABEL     KEY SEQUENCE              NOTES
        # 1st row --------------------------------------------------------------------------
        (0x0F0000,  'Run',   [Keycode.LEFT_SHIFT]),  # Run / Sprint
        (0x000F00,  ' W',    [Keycode.W]),           # Move Forward
        (0x0F0F0F,  'F ',    [Keycode.F]),           # Scope / Aim

        # 2nd row --------------------------------------------------------------------------
        (0x000F00,  ' A',    [Keycode.A]),           # Move Left
        (0x000F00,  ' S',    [Keycode.S]),           # Move Back
        (0x000F00,  'D ',    [Keycode.D]),           # Move Right

        # 3rd row --------------------------------------------------------------------------
        (0x000000,  ' E',    [Keycode.E]),           # Select
        (0x0F0F00,  'Jet',   [Keycode.SPACE]),       # Jetpack
        (0x000000,  'Esc',   [Keycode.ESCAPE]),      # Escape Key


        # 4th row --------------------------------------------------------------------------
        (0x0F000F,  ' G',    [Keycode.G]),           # Weapon Switch
        (0x00000F,  ' x',    [Keycode.X]),           # Menu 1
        (0x00000F,  'z ',    [Keycode.Z]),           # Menu 2
    ]
}
