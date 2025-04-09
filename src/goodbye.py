import random
from colorama import Fore
from load_dataset import load_dataset

def goodbye(user_entry):

    data = load_dataset('datasets/goodbyes.json')

    for goodbyes in data['goodbyes']:
        if user_entry in [pattern.lower() for pattern in goodbyes['patterns']]:
            response = random.choice(goodbyes['responses'])
            print(Fore.CYAN + response)
            return True
    return False