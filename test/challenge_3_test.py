import unittest

from challenge_3 import process_sokoban_move



class TestChallenge3(unittest.TestCase):

    def setUp(self):
        board = ["#############",
                "#p        * #",
                "#     b  b  #",
                "# *         #",
                "#############",
                ]


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_process_sokoban_move_exists(self):
        self.assertEqual(process_sokoban_move(), None)

    def test_returns_the_board(self):
        self.assertEqual(process_sokoban_move(board), board)

    def test_accepts_board_and_move(self):
        pass



if __name__ == "__main__":
    unittest.main()

