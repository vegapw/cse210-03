from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's Puzzle.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's Jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
        self._do_outputs()
        if (self._puzzle.is_puzzle_done()):
            print("You guessed, well done.")
        else: 
            print("ups, sorry!!, try again!!.")

    def _get_inputs(self):
        """Gets the letter or word to guess the puzzle.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
        size_letter = len(letter)
        if size_letter == 1:
            if self._puzzle.contain_letter(letter) and not self._puzzle.is_letter_used(letter):
                self._puzzle.reveal_letter_on_secret(letter)
            else:
                self._jumper.reduce_parachute()
            self._puzzle.add_used_letter(letter)
        else:
            if (size_letter > 1):
                if (self._puzzle.check_word_on_secret(letter)):
                    self._is_playing = False
                else:
                    self._puzzle.add_used_letter(letter)
                    self._jumper.reduce_parachute()
            else:
                self._jumper.reduce_parachute()

        
    def _do_updates(self):
        """Keeps watch on parachute and puzzle.

        Args:
            self (Director): An instance of Director.
        """
        if (self._puzzle.is_puzzle_done() or not self._jumper.is_alive()):
            self._is_playing = False
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        secret_word = self._puzzle.get_secret_hidden()
        for i in range(len(secret_word)):
            self._terminal_service.write_text_sep(secret_word[i]," ", " ")
        self._terminal_service.write_text("")
        self._terminal_service.write_text("")
        parachute = self._jumper.get_parachute()
        for j in range(len(parachute)):
            self._terminal_service.write_text_sep(parachute[j],"","\n")
        self._terminal_service.write_text("")
        self._terminal_service.write_text("")
        self._terminal_service.write_text("^^^^^^^")
        self._terminal_service.write_text("")
        self._terminal_service.write_text("")
        
        