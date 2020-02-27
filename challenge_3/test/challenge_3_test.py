import unittest

from challenge_3.app.challenge_3 import process_sokoban_move


class TestChallenge3(unittest.TestCase):

    def test_processes_legal_up_move(self):
        board_in = ["#############",
                    "#         * #",
                    "#p    b  b  #",
                    "# *         #",
                    "#############",]
        move = 'U'
        board_out = ["#############",
                     "#p        * #",
                     "#     b  b  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_processes_legal_down_move(self):
        board_in = ["#############",
                    "#         * #",
                    "#p    b  b  #",
                    "# *         #",
                    "#############",]
        move = 'D'
        board_out = ["#############",
                     "#         * #",
                     "#     b  b  #",
                     "#p*         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_processes_legal_right_move(self):
        board_in = ["#############",
                    "#         * #",
                    "#p    b  b  #",
                    "# *         #",
                    "#############",]
        move = 'R'
        board_out = ["#############",
                     "#         * #",
                     "# p   b  b  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_processes_legal_left_move(self):
        board_out = ["#############",
                     "#         * #",
                     "#p    b  b  #",
                     "# *         #",
                     "#############",]
        move = 'L'
        board_in = ["#############",
                    "#         * #",
                    "# p   b  b  #",
                    "# *         #",
                    "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_does_not_move_into_wall(self):
        board_in = ["#############",
                    "#         * #",
                    "#p    b  b  #",
                    "# *         #",
                    "#############",]
        move = 'L'
        board_out = ["#############",
                     "#         * #",
                     "#p    b  b  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_can_push_box_to_empty_square(self):
        board_in = ["#############",
                    "#         * #",
                    "#    pb  b  #",
                    "# *         #",
                    "#############",]
        move = 'R'
        board_out = ["#############",
                     "#         * #",
                     "#     pb b  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_can_push_box_to_storage_square(self):
        board_in = ["#############",
                    "#         * #",
                    "#    pb* b  #",
                    "# *         #",
                    "#############",]
        move = 'R'
        board_out = ["#############",
                     "#         * #",
                     "#     pB b  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_can_push_box_off_storage_square(self):
        board_in = ["#############",
                    "#         * #",
                    "#     pB b  #",
                    "# *         #",
                    "#############",]
        move = 'R'
        board_out = ["#############",
                     "#         * #",
                     "#      Pbb  #",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_cannot_push_box_thru_wall(self):
        board_in = ["#############",
                    "#         * #",
                    "#     b*  pb#",
                    "# *         #",
                    "#############",]
        move = 'R'
        board_out = ["#############",
                     "#         * #",
                     "#     b*  pb#",
                     "# *         #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)

    def test_can_push_two_boxes(self):
        board_in = ["#############",
                    "#     p   * #",
                    "#     B*   b#",
                    "# *   b     #",
                    "# *         #",
                    "#############",]
        move = 'D'
        board_out = ["#############",
                     "#         * #",
                     "#     P*   b#",
                     "# *   b     #",
                     "# *   b     #",
                     "#############",]
        self.assertEqual(process_sokoban_move(board_in, move), board_out)


if __name__ == "__main__":
    unittest.main()

