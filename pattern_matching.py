from enum import Enum, auto
from typing import Any


class A(Enum):
    one = auto()
    two = auto()
    three = auto()


def give_three_args(*args: Any) -> None:
    match args:
        case (int(), int(), int()):
            print("Three integer arguments!")
        case (str(), str(), str()):
            print("Three string arguments!")
        case (x, y, z) if type(x) == type(y) == type(z):
            print("Three arguments with same type")
        case (_, _, _):
            print("Three random arguments")
        case _:
            print("Not Allowed")


give_three_args(1, 2, 3)  # Three integer arguments!
give_three_args("yes", "no", "name")  # Three string arguments!
give_three_args(A.one, A.two, A.three)  # Three arguments with same type
give_three_args(1, "yes", A.one)  # Three random arguments
give_three_args(5)  # Not Allowed
give_three_args("hi", "hii")  # Not Allowed
