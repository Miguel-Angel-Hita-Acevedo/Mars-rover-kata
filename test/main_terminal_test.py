import unittest
from main_terminal import MainTerminal


class main_terminal_test(unittest.TestCase):
    def test_empty_parameters_then_dont_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute_command("")
        self.assertEqual("0:0:N", output)

    def test_one_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute_command("M")
        self.assertEqual("0:1:N", output)

    def test_one_move_turn_right_and_two_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute_command("MRMM")
        self.assertEqual("2:1:E", output)
