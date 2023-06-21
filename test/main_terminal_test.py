import unittest
from main_terminal import MainTerminal


class main_terminal_test(unittest.TestCase):
    def test_empty_parameters_then_dont_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("")
        self.assertEqual("0:0:N", output)

    def test_one_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("M")
        self.assertEqual("0:1:N", output)

    def test_one_move_turn_right_and_two_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("MRMM")
        self.assertEqual("2:1:E", output)

    def test_left_and_move_to_turn_around(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("LM")
        self.assertEqual("9:0:W", output)

    def test_left_twice_and_turn_around_with_final_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("LLMM")
        self.assertEqual("0:8:S", output)

    def test_turn_right_five_times_and_move(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("RRRRRM")
        self.assertEqual("1:0:E", output)
        
    def test_turn_left_five_times_and_turn_around(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("LLLLLLM")
        self.assertEqual("0:9:S", output)

    def test_move_up_ten_times_and_turn_around_to_initial_position(self):
        main_terminal = MainTerminal()
        output = main_terminal.execute("MMMMMMMMMM")
        self.assertEqual("0:0:N", output)