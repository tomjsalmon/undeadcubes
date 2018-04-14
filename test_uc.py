#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import unittest
import uc

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.die = uc.Die({'brains':3, 'shots':2, 'footsteps':1}, risk=2)

    def test_emojis(self):
        self.die.side_map = {
            'shots': '💥',
            'brains': '🧠',
            'footsteps': '👣'
        }
        self.assertEqual(self.die._Die__prettify('brains'), '🧠')
        self.assertEqual(self.die._Die__prettify('shots'), '💥')
        self.assertEqual(self.die._Die__prettify('footsteps'), '👣')

    def test_private_colours(self):
        self.die.colour_map = {
            1: '\033[0;37;42m',
            2: '\033[0;37;40m',
            3: '\033[0;37;41m'
        }
        self.die.risk = 1
        self.assertEqual(self.die._Die__colour(), ('\033[0;37;42m', uc.NORMAL_COLOUR))
        self.die.risk = 2
        self.assertEqual(self.die._Die__colour(), ('\033[0;37;40m', uc.NORMAL_COLOUR))
        self.die.risk = 3
        self.assertEqual(self.die._Die__colour(), ('\033[0;37;41m', uc.NORMAL_COLOUR))

    def test_public_colours(self):
        self.die.colour_map = {
            1: '\033[0;37;42m',
            2: '\033[0;37;40m',
            3: '\033[0;37;41m'
        }
        self.die.risk = 1
        self.assertEqual(self.die.colour(), ('\033[0;37;42m   %s' % uc.NORMAL_COLOUR))
        self.die.risk = 2
        self.assertEqual(self.die.colour(), ('\033[0;37;40m   %s' % uc.NORMAL_COLOUR))
        self.die.risk = 3
        self.assertEqual(self.die.colour(), ('\033[0;37;41m   %s' % uc.NORMAL_COLOUR))

    def test_roll(self):
        self.die.sides = {'brains':3, 'shots':2, 'footsteps':1}
        self.assertIn(self.die.roll(), ['brains', 'shots', 'footsteps'])

        self.die.sides = {'brains':5}
        self.die.risk = 1
        self.assertEqual(self.die.roll(), 'brains')
        self.assertEqual(self.die.roll_pretty(), ('\033[0;37;42m 🧠  %s' % uc.NORMAL_COLOUR))

        self.die.sides = {'shots':3}
        self.die.risk = 2
        self.assertEqual(self.die.roll(), 'shots')
        self.assertEqual(self.die.roll_pretty(), ('\033[0;37;40m 💥  %s' % uc.NORMAL_COLOUR))

        self.die.sides = {'footsteps':2}
        self.die.risk = 3
        self.assertEqual(self.die.roll(), 'footsteps')
        self.assertEqual(self.die.roll_pretty(), ('\033[0;37;41m 👣  %s' % uc.NORMAL_COLOUR))

if __name__ == '__main__':
    unittest.main()