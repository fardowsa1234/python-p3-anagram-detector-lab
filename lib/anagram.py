# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Ensure case-insensitivity

    def is_anagram(self, other_word):
        return sorted(self.word) == sorted(other_word.lower())  # Ensure case-insensitivity

    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]
