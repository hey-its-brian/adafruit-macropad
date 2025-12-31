# Brian Meyer 2025
# This has been created to use when managing folders on a remote server

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
app = {                    
    'name' : 'Media             ',     
    'macros' : [
        # COLOR          LABEL          KEY SEQUENCE                            NOTES
    # 1st row ----------------------------------------------------------------------------------------------
        (0x006666,      '  C',      [Keycode.COMMAND, 'c']),                  # Copy 
        (0x006666,      'V',        [Keycode.COMMAND, 'v']),                  # Paste
        (0x006600,      'Ent',      [Keycode.ENTER]),                         # ENTER key (dark green)
    # 2nd row ----------------------------------------------------------------------------------------------
        (0x006666,      '  X',      [Keycode.COMMAND, 'x']),                  # Cut
        (0x660000,      'del1',     [Keycode.COMMAND, Keycode.BACKSPACE]),    # Delete
        (0x660000,      'del2',     [Keycode.COMMAND, 'd']),                  # Confirm Delete
    # 3rd row ----------------------------------------------------------------------------------------------
        (0x665500,      'fldr',     [Keycode.CONTROL, Keycode.COMMAND, 'n']), # new folder with selection
        (0x665500,      'clstr',    [Keycode.COMMAND, 'u']),                  # clusters tracks in musicbrainz
        (0x660000,      '',         [Keycode.COMMAND, 'w',]),                 # Close window (deep red-brown)
    # 4th row ----------------------------------------------------------------------------------------------
        (0x660066,      'left',     [Keycode.LEFT_ARROW]),                    # left arrow
        (0x660066,      'dwn',      [Keycode.DOWN_ARROW]),                    # down arrow
        (0x660066,      'rght',     [Keycode.RIGHT_ARROW])                    # right arrow
    ]
}