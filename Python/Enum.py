# Enums are like Lookups 

from enum import Enum 



class State(Enum):
    INACTIVE =1
    ACTIVE = 2 


print(State.ACTIVE.value)
print(list(State))
print(len(State))

