import os
import sys
import time
import platform
import random
import logging

# Set up logging
logging.basicConfig(filename='program.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Attempt to import colorama, install it if not available
try:
    from colorama import Style, Fore, Back
except ModuleNotFoundError:
    logging.error("colorama module not found. Installing...")
    os.system("pip install colorama")
    from colorama import Style, Fore, Back

# Define color configurations
all_col = [
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.LIGHTCYAN_EX,
    Style.BRIGHT + Fore.LIGHTBLUE_EX,
    Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
    Style.BRIGHT + Fore.LIGHTYELLOW_EX,
]

all_DARKCOLORS = [
    Style.BRIGHT + Fore.CYAN,
    Style.BRIGHT + Fore.GREEN,
    Style.BRIGHT + Fore.RED,
    Style.BRIGHT + Fore.YELLOW,
    Style.BRIGHT + Fore.BLUE,
    Style.BRIGHT + Fore.WHITE,
]

ran = random.choice(all_DARKCOLORS)
ran2 = random.choice(all_col)

# Define specific colors
lg = Style.BRIGHT + Fore.LIGHTGREEN_EX
g = Style.BRIGHT + Fore.GREEN
lc = Style.BRIGHT + Fore.LIGHTCYAN_EX
c = Style.BRIGHT + Fore.CYAN
ly = Style.BRIGHT + Fore.LIGHTYELLOW_EX
y = Style.BRIGHT + Fore.YELLOW
r = Style.BRIGHT + Fore.RED
lr = Style.BRIGHT + Fore.LIGHTRED_EX
b = Style.BRIGHT + Fore.BLUE
w = Style.BRIGHT + Fore.LIGHTWHITE_EX

# Define the logo with ASCII art
logo = f"""
                               ▄█     ▄███████▄                          
                              ███    ███    ███                          
                              ███▌   ███    ███                          
                              ███▌   ███    ███                          
                              ███▌ ▀█████████▀                           
                              ███    ███                                 
                              ███    ███                                 
                              █▀    ▄████▀                               
                                                                         
   ▄████████    ▄████████  ▄█    █▄     ▄████████    ▄████████  ▄█       
  ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ███       
  ███    ███   ███    █▀  ███    ███   ███    █▀    ███    ███ ███       
 ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███  ▄███▄▄▄       ███    ███ ███       
▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀     ▀███████████ ███       
▀███████████   ███    █▄  ███    ███   ███    █▄    ███    ███ ███       
  ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ███▌    ▄ 
  ███    ███   ██████████  ▀██████▀    ██████████   ███    █▀  █████▄▄██ 
  ███    ███                                                   ▀         
                 </> Author: Kunal-Namdas    
                 </> GitHub : @kunalnamdas                                                                                                      
"""

# Function to print the banner with the logo
def banner():
    print(ran + logo)

# Function to clear the console screen
def clear():
    try:
        s = platform.platform()
        if "Windows" in s:
            os.system("cls")
        else:
            os.system("clear")
    except Exception as e:
        logging.error("Failed to clear the screen: %s", e)
        print("Error clearing the screen:", e)

# Function to print a string with a typing effect
def sprint(text):
    try:
        for i in text + c + "\n":
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(3/90)
    except Exception as e:
        logging.error("Error during typing effect: %s", e)
        print("Error in sprint function:", e)

# Function to execute a system command
def command(command_str):
    try:
        os.system(command_str)
    except Exception as e:
        logging.error("Error executing command '%s': %s", command_str, e)
        print("Error executing command:", e)

# Main program function
def program():
    import ipapi
    try:
        clear()
        banner()

        ip = input(ran + "Enter target IP: " + c)
        location = ipapi.location(ip)

        for k, v in location.items():
            print(c + k + " : " + lr + str(v))
    except Exception as e:
        logging.error("Error in program function: %s", e)
        print("Error in program function:", e)

# Loop to continue or stop the program based on user input
def main():
    yes = ['y', 'yes']
    no = ['n', 'no']

    cont = ""
    while cont not in no:
        try:
            program()
            cont = input(lg + "Do you want to continue? [y/n]: " + c)
            if cont in no:
                clear()
                print("Program terminated successfully.")
                logging.info("Program terminated successfully.")
            else:
                clear()
                banner()
        except KeyboardInterrupt:
            clear()
            print("\nProgram terminated successfully.")
            logging.info("Program terminated successfully.")
            break
        except Exception as e:
            logging.error("Error in main loop: %s", e)
            print("Error in main loop:", e)

if __name__ == "__main__":
    main()
