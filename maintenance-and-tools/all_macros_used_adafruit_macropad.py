(0x002000, 'C', [Keycode.COMMAND, 'c',-Keycode.COMMAND]),       # Copy
(0x002000, 'V', [Keycode.COMMAND, 'v',-Keycode.COMMAND]),       # Paste
(0x002000, 'X  ', [Keycode.COMMAND, 'x',-Keycode.COMMAND]),     # Cut
(0x002000, 'Clr  ', [Keycode.COMMAND, 'k',-Keycode.COMMAND]),   # Clear terminal
(0x202000, 'undo', [Keycode.COMMAND, 'z',-Keycode.COMMAND]),    # Undo
(0x202000, 'redo', [Keycode.COMMAND, 'y',-Keycode.COMMAND]),    # Redo
(0x000020, '+ Tab', [Keycode.COMMAND, 't',-Keycode.COMMAND]),   # Add tab (Safari, etc)
(0x000020, '- Tab', [Keycode.COMMAND, 'w',-Keycode.COMMAND]),   # Close tab
(0x300000, 'show', [Keycode.COMMAND,Keycode.CONTROL,Keycode.OPTION,Keycode.SHIFT,':',-Keycode.COMMAND,-Keycode.CONTROL,-Keycode.OPTION,-Keycode.SHIFT]),     # Show desktop
(0x101010, 'Spot', [Keycode.COMMAND,Keycode.SPACEBAR,-Keycode.COMMAND,-Keycode.SPACEBAR]),   # Spotlight     
(0x000020, 'Ent', [Keycode.ENTER,-Keycode.ENTER]),              # Enter key
(0x300000, '[ ]', [Keycode.CONTROL,Keycode.UP_ARROW,-Keycode.CONTROL,-Keycode.UP_ARROW]), #Expose
(0x111111, '< >', ['<pre><code class="ruby">',-Keycode.COMMAND]),    # Ruby Pre Open
(0x002000, '</ ', ['</code></pre> ',-Keycode.COMMAND]),              # Reby Pre Close
(0x004000, 'Website Name', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'websitename.com\n']),                        # Open website in new tab
(0x101010, 'Safari', [Keycode.COMMAND,Keycode.SPACEBAR,-Keycode.COMMAND,-Keycode.SPACEBAR,'','','safari',Keycode.ENTER]),  # Open Safari/application
(0x111111, 'Save', [Keycode.COMMAND,'s',-Keycode.COMMAND]),    # Save
(0x002000, 'close', [Keycode.COMMAND, 'w',-Keycode.COMMAND]),   # Close window/tab
(0x000020, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),   # Media - vol up
(0x101010, 'Music', [Keycode.COMMAND,Keycode.SPACEBAR,-Keycode.COMMAND,-Keycode.SPACEBAR,'','','music',Keycode.ENTER,-Keycode.ENTER]),                                          # launch music app
(0x000020, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),   # Media - vol down
(0x101010, 'Podcast', [Keycode.COMMAND,Keycode.SPACEBAR,-Keycode.COMMAND,-Keycode.SPACEBAR,'','','podcasts',Keycode.ENTER,-Keycode.ENTER]),                                 # launch podcasts app
(0x200000, 'Mute', [[ConsumerControlCode.MUTE]]),       # Media - mute
(0x000000, '', []),                                     # BLANK
(0x202000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),  # Media - prev. track
(0x002000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),   # Media - Play/pause
(0x202000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),  # Media - Next track
(0x000000, '', [Keycode.COMMAND,'q',-Keycode.COMMAND])      # Quit
# Numberpad Layout:
# 1st row ----------
        (0x202000, '7', ['7']),
        (0x202000, '8', ['8']),
        (0x202000, '9', ['9']),
        # 2nd row ----------
        (0x202000, '4', ['4']),
        (0x202000, '5', ['5']),
        (0x202000, '6', ['6']),
        # 3rd row ----------
        (0x202000, '1', ['1']),
        (0x202000, '2', ['2']),
        (0x202000, '3', ['3']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x800000, '0', ['0']),
        (0x101010, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])

                         
                           
                           
                           
                           
                           
                           