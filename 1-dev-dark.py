# Brian Meyer 2022
# This macro is for my dev work and is specialized for that.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
app = {                    
    'name' : '1-Dev-Night',     
    'macros' : [
        # COLOR                 LABEL                 KEY SEQUENCE                      NOTES
        # 1st row ----------------------------------------------------------------------------------------------
        (0x003333,              '  C',            [Keycode.COMMAND, 'c']),              # Copy (very dark teal)
        (0x003333,              'V',              [Keycode.COMMAND, 'v']),              # Paste
        (0x003300,              'Ent',            [Keycode.ENTER]),                     # ENTER key (forest-shadow green)
        # 2nd row ----------------------------------------------------------------------------------------------
        (0x003333,              '  X',            [Keycode.COMMAND, 'x']),              # Cut
        (0x263340,              'undo',           [Keycode.COMMAND, 'z']),              # Undo last command (stormy slate blue)
        (0x330000,              'Clr',            [Keycode.COMMAND, 'k']),              # Clear terminal (oxblood)
        # 3rd row ----------------------------------------------------------------------------------------------
        (0x332B00,              '< >',            ['<pre><code class="ruby">']),        # Open Redmine Code (burnt ochre)
        (0x332B00,              '</ >',           ['</code></pre> ',]),                 # Close Redmine Code
        (0x330000,              'Close',          [Keycode.COMMAND, 'w',]),             # Close window (oxblood)
        # 4th row ----------------------------------------------------------------------------------------------
        (0x330033,              'esc',            [Keycode.ESCAPE]),                    # escape (wine purple)
        (0x330000,              'del',            [Keycode.DELETE]),                    # Delete
        (0x003300,              'Save',           [Keycode.COMMAND,'s'])                # Save (forest-shadow green)
    ]
}