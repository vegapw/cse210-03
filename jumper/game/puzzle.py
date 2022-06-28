import random

class Puzzle:
    """The puzzle to be solve before the jumper falls. 
    
    The responsibility of Puzzle is to select a random word from a list and hide it from the player. 
    
    Attributes:
        _secret_word (string): The the secret word, selected from a list.
        _secret_word_hidden List[str]: An array with the same length 
        of the secret word, but with a character '_' on each space.
        _used_letters List(str): An array with the letters and words used.
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        list_secret_words = ["Unknown", "VideoGame", "Universe", "Gospel", "Plan"]
        self._secret_word = list_secret_words[random.randint(1, len(list_secret_words))-1].lower()
        self._secret_word_hidden = []
        for i in range(len(self._secret_word)):
            self._secret_word_hidden.append("_")
        self._used_letters = []
    
    def get_secret_hidden(self):
        """Gets the secret hidden.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: the secret word hidden.
        """
        return self._secret_word_hidden

    def contain_letter(self, letter):
        """verifies if a letter is contained in the secret word and return a boolean value.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter : any letter from a to z
            
        Returns:
            boolean: True if the secret word contains the letter, otherwise False.
        """
        return True if self._secret_word.find(letter) != -1 else False
        
    def reveal_letter_on_secret(self, letter):
        """mark the letter on secret word hidden if it exist.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter : letter to be marked in the secret word hidden
        """
        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter:
                self._secret_word_hidden[i] = letter

    def check_word_on_secret(self, word):
        """check if the word is equals to the secret word.

        Args:
            self (Puzzle): An instance of Puzzle.
            word : word to compare with secret word
        """
        if word == self._secret_word:
            self._secret_word_hidden = self._secret_word
            return True
        else:
            return False
        
    def add_used_letter(self, word):
        """add the word or letter used to have a control of used letters.

        Args:
            self (Puzzle): An instance of Puzzle.
            word : letter or word to be added in the array of used letters.
        """
        self._used_letters.append(word)
    
    def is_letter_used(self, letter):
        """verifies if a letter is contained in the used_letters array.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter : any letter from a to z.
            
        Returns:
            boolean: True if the letter is contained in the array, otherwise False.
        """
        try:
            value = self._used_letters.index(letter)
            if value >= 0:
                return True
        except ValueError as ex:
            return False
    
    def is_puzzle_done(self):
        """verifies if a letter is contained in the secret word and return a boolean value.

        Args:
            self (Puzzle): An instance of Puzzle.
            
        Returns:
            boolean: True if the character "_" is not found in the secret word hidden, 
            otherwise False.
        """
        try:
            value = self._secret_word_hidden.index("_")
            if value >= 0:
                return False
        except ValueError as ex:
            return True