class Phoneme():
    """docstring for ."""
    def __init_(self, arg):
        self.arg = arg

class Vowel(Phoneme):
    """docstring for Vowel."""
    def __init__(self, arg):
        super(Vowel, self).__init__()
        self.arg = arg

class Consonant(Phoneme):
    """docstring for Consonant."""
    def __init__(self, arg):
        super(Consonant, self).__init__()
        self.arg = arg


phonetic_correspondences = {
    "a" : ["a"],
    "b" : ["b", "v"],
    "s" : ["s", "c"],
    "k" : ["c", "qu", "k"],
    "c" : ["k"]
}

def parse_text(text):
    parsed_text = ""
    for letter in text:
        parsed_text += phonetic_correspondences.get(letter)
    return parsed_text

#def assign_phoneme(word):

for letter in "casa":
    print(phonetic_correspondences.get(letter, "Sound is not found"))
