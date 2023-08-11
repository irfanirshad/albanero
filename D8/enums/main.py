from enum import Enum, auto

from typing import Optional, List

class State(Enum):
    PLAYING =  auto() 
    PAUSED = auto()
    GAME_OVER = auto()
    
state = State.PLAYING


# could use it like this....
if state == State.PLAYING:
    pass



class 