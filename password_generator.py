import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
combo_list = letters + numbers + symbols


class RandomPassword:
    """Create a randomized 15-character password"""
    def __init__(self):
        self.key_list = []

    def generate(self):
        self.key_list = []
        for i in range(15):
            random_letter = random.choice(combo_list)
            self.key_list.append(random_letter)
        password = ''.join(self.key_list)
        return password
