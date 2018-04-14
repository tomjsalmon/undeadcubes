#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
Undead Cubes
"""
import random
from typing import Dict, List, Tuple

NORMAL_COLOUR = '\033[0;0m'

class Die:
    """This class represents a die in the game"""
    def __init__(self,
                 sides: Dict[str, int],
                 risk: int,
                 side_map: Dict[str, str] = None,
                 colour_map: Dict[int, str] = None) -> None:
        self.sides = sides
        self.risk = risk

        if side_map:
            self.side_map = side_map
        else:
            # Use the default
            self.side_map = {
                'shots': '💥',
                'brains': '🧠',
                'footsteps': '👣'
            }

        if colour_map:
            self.colour_map = colour_map
        else:
            # Use the default
            self.colour_map = {
                1: '\033[0;37;42m',
                2: '\033[0;37;40m',
                3: '\033[0;37;41m'
            }

    def __colour(self) -> Tuple[str, str]:
        """
        Spit out the colour assocated with the die's
            risk, and the normal terminal colour. We
            return a tuple so it can be used in other
            methods to wrap around stuff.
        """
        return(self.colour_map[self.risk], NORMAL_COLOUR)

    def __prettify(self, side: str) -> str:
        """
        Spit out an emotion corresponding with the
            string of the side given as an arg.
        """
        return self.side_map[side]

    def roll(self) -> str:
        """
        Roll the die. We make a list containing each
            side, then we pick a random number from
            the list and return the string at that
            position.
        """
        possibilities: List[str] = []
        for side_type in self.sides:
            for _ in range(self.sides[side_type]):
                possibilities.append(side_type)
        minimum = 0
        maximum: int = len(possibilities) - 1
        top_side = random.randint(minimum, maximum)
        return possibilities[top_side]

    def roll_pretty(self) -> str:
        """
        Roll the die using the roll() method, then
            turn the answer into an emotion with
            the die's risk as a background colour.
        """
        result = self.roll()
        emoji = self.__prettify(result)
        die_colour, normal_colour = self.__colour()
        return '%s %s  %s' % (die_colour, emoji, normal_colour)

    def colour(self) -> str:
        """
        Spit out the colour of the die as a single
            string (instead of a Tuple).
        """
        return '%s   %s' % self.__colour()
