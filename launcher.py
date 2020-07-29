from utils.helperfuncs import launch_ai
from termcolor import colored
import colorama
import time
from pynput.keyboard import Key

colorama.init()

capture_box = (644,308,1279,443)
print(colored("""
  _____  _                _____                                 _ 
 |  __ \(_)              / ____|                          /\   (_)
 | |  | |_ _ __   ___   | |  __  __ _ _ __ ___   ___     /  \   _ 
 | |  | | | '_ \ / _ \  | | |_ |/ _` | '_ ` _ \ / _ \   / /\ \ | |
 | |__| | | | | | (_) | | |__| | (_| | | | | | |  __/  / ____ \| |
 |_____/|_|_| |_|\___/   \_____|\__,_|_| |_| |_|\___| /_/    \_\_|
                                                                                                                                                                                
                                      
                                     ██  By Fwiz - (Github.com/fwizzz) ██ 
                                     
For any help regarding this project
Contact me on discord = fwiz#0003                                   
                                                                            
""",color = "green"))


response =  input(colored('To Open up the game on google chrome and click type "start"',color="yellow"))


from utils.model import model


if response == "start":
    time.sleep(2)
    print("(3) launching Ai")
    launch_ai(model,0.08,capture_box,Key.space,Key.caps_lock)
    print("(4) Ai Launched")
