from StringIO import StringIO

import unittest
from trivia import Game
from mock import patch


class TestGame(unittest.TestCase):
    def test_create_rock_question(self):
        game = Game()
        res = game.create_rock_question(5)
        assert res == "Rock Question 5"

    def test_is_playable(self):
        game = Game()
        assert game.is_playable() == False
        game.add("Player1")
        assert game.is_playable() == False
        game.add("Player2")
        assert game.is_playable() == True

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_player(self, stdout):
        game = Game()
        res = game.add("Player")
        assert res
        assert stdout.getvalue() == "Player was added\nThey are player number 1\n"

unittest.main()
