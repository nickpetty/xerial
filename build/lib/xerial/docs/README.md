
xerial - Terminal Based Serial Client
-------------------------------------
 + URL: http://github.com/nickpetty/xserial

    xerial Copyright (C) 2016  Nicholas Petty
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `xerial -license' for details.

Usage:
------------------------------------------------------------------------
    -p <port>              # Connect to serial port.
    -a <b/p/s>             # -a bytesize/parity/stopbits (default 8/N/1).
                           # Parity options 'N','E','O','M','S'.
    -b <speed/baudrate>    # 9600, 115200, etc.
    -CR                    # Carriage Return '\r'.
    -LF                    # Linefeed (newline) '\n'.
    -hw                    # Enable Hardware Handshake (rtscts).
    -ls                    # List available ports.
    -t <seconds>           # Timeout (in seconds).
    -s <presetName>        # Save flags to preset file. Must be the last flag. Will not connect with flag.
                           # Usage: i.e., xerial -c /dev/tty.usbserial-A01293 -b 115200 -CR -s myPreset
    -l <presetName>        # Load preset.  Usage: xerial -l myPreset
    -lp                    # List presets in preset folder
                           # Optional: '-lp <presetname>' Lists parameters for given preset.
    -h                     # This menu.
    -log                   # Log all terminal activity to file in current working directory.
    -license               # Display License

Notes:
------------------------------------------------------------------------
 + Type '>q' at anytime to exit serial terminal