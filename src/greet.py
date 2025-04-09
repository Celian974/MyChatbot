import random
from colorama import Fore
from load_dataset import load_dataset

def greet(user_entry):

    data = load_dataset('datasets/greetings.json')

    for greetings in data['greetings']:
        if user_entry in [pattern.lower() for pattern in greetings['patterns']]:
            response = random.choice(greetings['responses'])
            print(Fore.CYAN + response)
            return True
    return False