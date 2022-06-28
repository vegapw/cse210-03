
class Jumper:
    """The player represented as a jumper with a parachute. 
    
    The responsibility of a Jumper is to keep track of its parachute.
    
    Attributes:
        tries (int): amount of permited mistakes before the parachute disappears.
        parachute List(str) : the Jumper painted in an array.
        parachute_end List(str) : the Jumper death painted in an array.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._tries = 4
        self._parachute = [
            " ___",
            "/___\\",
            "\\   /",
            " \\ /",
            "  0",
            " /|\\",
            " / \\",
        ]
        self._parachute_end = [
            "  X",
            " /|\\",
            " / \\",
        ]

    def get_parachute(self):
        """Gets the parachute array.
        
        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            Array str: The current parachute.
        """
        return self._parachute

        
    def reduce_parachute(self):
        """reduce the number of tries, and erase the top of the parachute.
        if the the tries attribute reach zero, the parachute is totally erased
        and the player go dead

        Args:
            self (Jumper): An instance of Jumper.
        
        """
        if self._tries > 0:
            self._tries -= 1
            self._parachute.pop(0)
        if self._tries == 0:
            self._parachute = self._parachute_end

    def is_alive(self):
        """Check if the parachute still remains and the player is alive.

        Args:
            self (Jumper): An instance of Jumper.
        
        Returns:
            True if there are tries remaining, if not return false with the jumper death
        """

        return True if self._tries > 0 else False
