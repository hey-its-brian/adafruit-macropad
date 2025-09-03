# Brian Meyer 2025
# This macro is for my dev work and is specialized for that.

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    
    'name' : '1-Dev',     
    'macros' : [
        # COLOR     LABEL         KEY SEQUENCE                    NOTES
        # 1st row ----------------------------------------------------------------------------------------------
        (0x000F0F, '  C',   [Keycode.COMMAND, 'c']),              # Copy
        (0x000F0F, 'V',     [Keycode.COMMAND, 'v']),              # Paste
        (0x0F000F, 'Ent',   [Keycode.ENTER]),                     # ENTER key
        # 2nd row ----------------------------------------------------------------------------------------------
        (0x202000, 'undo',  [Keycode.COMMAND, 'z']),              # Undo last command
        (0x202000, 'redo',  [Keycode.COMMAND, 'y']),              # Redo last command
        (0x0F0000, 'Clr',   [Keycode.COMMAND, 'k']),              # Clear terminal
        # 3rd row ----------------------------------------------------------------------------------------------
        (0x0F0F0F, '< >',   ['<pre><code class="ruby">']),        # Open Redmine Code
        (0x0F0F0F, '</ > ', ['</code></pre> ',]),                 # Close Redmine Code
        (0x0F0000, 'Close', [Keycode.COMMAND, 'w',]),             # Close window
        # 4th row ----------------------------------------------------------------------------------------------
        (0x0F0F00, 'esc',   [Keycode.ESCAPE]),                    # escape
        (0x0F000F, 'X',     [Keycode.COMMAND,'x']),               # Cut
        (0x000F00, 'Save',  [Keycode.COMMAND,'s'])                # Save
    ]
}
