from StringIO import StringIO
from approvaltests import Approvals
from approvaltests.TextDiffReporter import TextDiffReporter
import os
from mock import patch
import unittest

from trivia import Game

os.environ['APPROVALS_TEXT_DIFF_TOOL'] = 'meld'

reporter = TextDiffReporter()


class TextGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test(self, stdout):
        game = Game()
        game.add('one')
        game.add('two')
        Approvals.verify(stdout.getvalue(), reporter)

    @patch('sys.stdout', new_callable=StringIO)
    def test_one(self, stdout):
        randrange = [1, 6, 2, 1, 3, 6, 1, 3, 1, 3, 5, 1, 2, 6, 7, 1, 7, 2, 3, 1, 2, 3, 1, 3, 2, 1, 2, 3, 5, 1, 2, 3, 5,
                     4]
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')
        game.is_playable()

        while randrange:
            game.roll(randrange.pop() + 1)

            if randrange.pop() == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.was_correctly_answered()

            if not not_a_winner: break

        Approvals.verify(stdout.getvalue(), reporter)

    @patch('sys.stdout', new_callable=StringIO)
    def test_two(self, stdout):
        randrange = [1, 6, 7, 1, 2, 3, 4, 5, 3, 1, 2, 3, 6, 2, 4, 7, 4, 2, 1, 3, 6, 4, 3, 2, 4, 7, 2, 4]
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')
        game.is_playable()

        while randrange:
            game.roll(randrange.pop() + 1)

            if randrange.pop() == 7:
                not_a_winner = game.wrong_answer()
            else:
                not_a_winner = game.was_correctly_answered()

            if not not_a_winner: break

        Approvals.verify(stdout.getvalue(), reporter)

    @patch('sys.stdout', new_callable=StringIO)
    def test_three(self, stdout):
        randrange = [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0,
                     0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 2]
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')
        game.is_playable()

        while randrange:
            game.roll(randrange.pop() + 1)

            not_a_winner = game.wrong_answer()

            if not not_a_winner: break

        Approvals.verify(stdout.getvalue(), reporter)


unittest.main()
