# Brian Meyer 2022
# This macro is for my dev work and is specialized for that.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
app = {                    
    'name' : '1-Dev',     
    'macros' : [
        # COLOR                 LABEL                 KEY SEQUENCE                      NOTES
        # 1st row ----------------------------------------------------------------------------------------------
        (0x006666,              '  C',            [Keycode.COMMAND, 'c']),              # Copy (dim teal)
        (0x006666,              'V',              [Keycode.COMMAND, 'v']),              # Paste
        (0x006600,              'Ent',            [Keycode.ENTER]),                     # ENTER key (dark green)
        # 2nd row ----------------------------------------------------------------------------------------------
        (0x006666,              '  X',            [Keycode.COMMAND, 'x']),              # Cut
        (0x4C6A80,              'undo',           [Keycode.COMMAND, 'z']),              # Undo last command (dusty blue-grey)
        (0x660000,              'Clr',            [Keycode.COMMAND, 'k']),              # Clear terminal (deep red-brown)
        # 3rd row ----------------------------------------------------------------------------------------------
        (0x665500,              '< >',            ['<pre><code class="ruby">']),        # Open Redmine Code (muted mustard)
        (0x665500,              '</ >',           ['</code></pre> ',]),                 # Close Redmine Code
        (0x660000,              'Close',          [Keycode.COMMAND, 'w',]),             # Close window (deep red-brown)
        # 4th row ----------------------------------------------------------------------------------------------
        (0x660066,              'esc',            [Keycode.ESCAPE]),                    # escape (dark plum)
        (0x660000,              'del',            [Keycode.DELETE]),                    # Delete
        (0x006600,              'Save',           [Keycode.COMMAND,'s'])                # Save (dark green)
    ]
}