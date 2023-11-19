# Ross Hamey
# CSE163 - P9.5
# 11/12/2023
# https://github.com/Endeared

import random

history = []

 # All doctors share the same qualifiers, replacements, and hedges.

QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                'Did I just hear you say that ',
                'Why do you believe that ']

REPLACEMENTS = {'i': 'you', 'me': 'you', 'my': 'your',
                'we': 'you', 'us': 'you', 'am': 'are',
                'you': 'i', 'you': 'I'}

HEDGES = ['Go on.', 'I would like to hear more about that.',
            'And what do you think about this?', 'Please continue.'] 

class Doctor(object):

    def __init__(self):
        self.qualifiers = QUALIFIERS
        self.replacements = REPLACEMENTS
        self.hedges = HEDGES

    def greeting(self):
        return "Hello, how can I help you today?"
    
    def farewell(self):
        return "Have a nice day!"

    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1, 2):
            # Just hedge
            answer = random.choice(self.hedges)
        elif probability == 3 and len(history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
                    self.changePerson(random.choice(history))
        else:
            # Transform the current input
            answer = random.choice(self.qualifiers) + self.changePerson(sentence)
        # Always add the current sentence to the history list
        history.append(sentence)
        return answer

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person
        pronouns."""
        doctor = Doctor()
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word, word))
        return " ".join(replyWords) 

def main():
    """Handles the interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    doctor = Doctor()
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(doctor.reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()

