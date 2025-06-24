import sys
import time
import shutil


### eksperimen
### bisa dicoba2 juga buat yang lain

def start_menu_interface():
    logo = '''
 ██████╗ ██╗    ██╗ ██████╗ █████╗ 
██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║   ██║██║ █╗ ██║██║     ███████║
██║   ██║██║███╗██║██║     ██╔══██║
╚██████╔╝╚███╔███╔╝╚██████╗██║  ██║
 ╚═════╝  ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝ 
 
[ Login ]   [ Help ]   [ Register ]   [ Menu ]   [ Logout ]

                              [Exit]                                
'''
    return logo

def print_centered_start(text):
    """Prints text centered in the terminal."""
    cols = shutil.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        padding = " " * ((cols - len(line)) // 2)
        print(padding + line)

import os

import os

def print_centered_menu(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Find the maximum line length
    max_line_length = max(len(line) for line in text.splitlines())
    
    # Calculate left padding
    left_padding = (terminal_width - max_line_length) // 2
    
    # Print the text with left padding
    print('\n'.join([' ' * left_padding + line for line in text.splitlines()]))

# Define ASCII art
def ascii_art():
    ascii_art = """
                                         *******
                                              ~             *---*******
                                             ~             *-----*******
                                      ~                   *-------*******
                                     __      _   _!__     *-------*******
                                _   /  \_  _/ \  |::| ___ **-----********   ~
                              _/ \_/^    \/   ^\/|::|\|:|  **---*****/^\_
                           /\/  ^ /  ^    / ^ ___|::|_|:|_/\_******/  ^  
                          /  \  _/ ^ ^   /    |::|--|:|---|  \__/  ^     ^\___
                        _/_^  \/  ^    _/ ^   |::|::|:|-::| ^ /_  ^    ^  ^   \_
                       /   \^ /    /\ /       |::|--|:|:--|  /  \        ^      
                      /     \/    /  /        |::|::|:|:-:| / ^  \  ^      ^     
                _Q   / _Q  _Q_Q  / _Q    _Q   |::|::|:|:::|/    ^ \   _Q      ^
               /_\)   /_\)/_/\\)  /_\)  /_\)  |::|::|:|:::|          /_\)
            _O|/O___O|/O_OO|/O__O|/O__O|/O__________________________O|/O__________
           //////////////////////////////////////////////////////////////////////

                            Welcome to the Danville!

        [1] Inventory
        [2] Battle
        [3] Arena
        [4] Laboratory
        [5] Shop
        [6] Back
                            
    """
    return ascii_art

def menu_interface():
    menu = '''
    [1] Inventory
    [2] Battle
    [3] Arena
    [4] Laboratory
    [5] Back
    '''
def admin_menu_interface():
    admin_ai='''
                                  _  _|_  _    \.    .  /    _  _|_  _
                                 |;|_|;|_|;|    \:. ,  /    |;|_|;|_|;|
                                 \..      /    ||;   . |    \.    .  /
                                  \.  ,  /     ||:  .  |     \:  .  /
                                   ||:   |_   _ ||_ . _ | _   _||:   |
                                   ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                                   ||:   ||.    .     .      . ||:  .|
                                   ||: . || .  Hello, Admin  , ||:   |       \,/
                                   ||:   ||:  ,  _______   .   ||: , |            /`
                                   ||:   || .   /+++++++\    . ||:   |
                                   ||:   ||.    |+++++++| .    ||: . |
                                __ ||: . ||: ,  |+++++++|.  . _||_   |
                       ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
                  -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
                      [1] Monster Management
                      [2] Shop Management
                      [3] Back

    '''
        # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Calculate the indentation needed for centering
    indentation = (terminal_width - max(len(line) for line in admin_ai.split('\n'))) // 2

    # Print the ASCII art with the calculated indentation
    print('\n'.join(' ' * indentation + line for line in admin_ai.split('\n')))

if __name__ =='__main__':
    admin_menu_interface()
    # print_centered(main_menu_interface())
    