# Brian Meyer 2022
# This is a test of various colors to see how they look

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    
    'name' : 'Colors            ',     
    'macros' : [
        # COLOR       LABEL       VALUE                                
    # 1st row ---------------------
        (0xFF0000,   'red',     ['red']),           
        (0x00FF00,   'green',   ['green']),            
        (0x0000FF,   'blue',    ['blue']),               
    # 2nd row ---------------------
        (0x00FFFF,   'cyan',    ['cyan']),          
        (0xFF00FF,   'magenta', ['magenta']),            
        (0xFFFF00,   'yellow',  ['yellow']),           
    # 3rd row ---------------------
        (0xFFA500,   'orange',  ['orange']),      
        (0x800080,   'purple',  ['purple']),         
        (0xFFC0CB,   'pink',    ['pink']),      
    # 4th row ---------------------
        (0x90EE90,   'ltGreen', ['Light Green']),
        (0x008080,   'teal',    ['teal']),
        (0x228B22,   'green2',  ['Forest Green'])
    ]
}

