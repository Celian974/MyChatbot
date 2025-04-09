from colorama import Fore
import random
from load_dataset import load_dataset
from greet import greet
from goodbye import goodbye


print(Fore.CYAN + "Welcome to this simple Chatbot. Type \'exit\' or \'quit\' to end the program.")

end_chat = ["quit", "exit"]

while True:
    user_entry = input(Fore.WHITE + ">>> ").strip().lower()

    if user_entry in end_chat:
        print(Fore.LIGHTBLACK_EX + "Exiting Chatbot...")
        break

    if greet(user_entry):
        found_match = True
    elif goodbye(user_entry):
        found_match = True
        confirmation = input(Fore.YELLOW + "Do you really want to end the chat ? [yes/no] : ")
        if confirmation in ["yes", "y"]:
            print(Fore.LIGHTBLACK_EX + "Exiting Chatbot...")
            break
        elif confirmation in ["no", "n"]:
            pass
        else:
            print(Fore.RED + "Sorry I didn't understand that. Aborting...")

    else:
        print(Fore.RED + "Sorry, I didn't understand that.")
