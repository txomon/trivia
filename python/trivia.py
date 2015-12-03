#!/usr/bin/env python

class Game:
    def __init__(self):
        self.players = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append('Pop Question %s' % i)
            self.science_questions.append('Science Question %s' % i)
            self.sports_questions.append('Sports Question %s' % i)
            self.rock_questions.append('Rock Question %s' % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(
            {
                'name': player_name,
                'place': 0,
                'gold': 0,
                'in_penalty_box': False,
            }
        )

        print '%s was added' % player_name
        print 'They are player number %s' % len(self.players)

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        player = self.players[self.current_player]['name']
        print '%s is the current player' % player
        print 'They have rolled a %s' % roll

        if self.players[self.current_player]['in_penalty_box']:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print '%s is getting out of the penalty box' % player
                self.move_player(roll)

            else:
                print '%s is not getting out of the penalty box' % player
                self.is_getting_out_of_penalty_box = False
                return
        else:
            self.move_player(roll)

        print "%s's new location is %d" % (
            player,
            self.players[self.current_player]['place']
        )
        print 'The category is %s' % self._current_category
        self._ask_question()

    def move_player(self, roll):
        self.players[self.current_player]['place'] += roll
        if self.players[self.current_player]['place'] > 11:
            self.players[self.current_player]['place'] -= 12

    def _ask_question(self):
        if self._current_category == 'Pop': print self.pop_questions.pop(0)
        if self._current_category == 'Science': print self.science_questions.pop(0)
        if self._current_category == 'Sports': print self.sports_questions.pop(0)
        if self._current_category == 'Rock': print self.rock_questions.pop(0)

    @property
    def _current_category(self):
        if self.players[self.current_player]['place'] == 0: return 'Pop'
        if self.players[self.current_player]['place'] == 1: return 'Science'
        if self.players[self.current_player]['place'] == 2: return 'Sports'
        if self.players[self.current_player]['place'] == 4: return 'Pop'
        if self.players[self.current_player]['place'] == 5: return 'Science'
        if self.players[self.current_player]['place'] == 6: return 'Sports'
        if self.players[self.current_player]['place'] == 8: return 'Pop'
        if self.players[self.current_player]['place'] == 9: return 'Science'
        if self.players[self.current_player]['place'] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        player = self.players[self.current_player]['name']
        if self.players[self.current_player]['in_penalty_box']:
            if self.is_getting_out_of_penalty_box:
                print 'Answer was correct!!!!'
                self.players[self.current_player]['gold'] += 1
                print '%s now has %d Gold Coins.' % (
                    player, self.players[self.current_player]['gold'])

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            print 'Answer was corrent!!!!'
            self.players[self.current_player]['gold'] += 1
            print '%s now has %d Gold Coins.' % (
                player, self.players[self.current_player]['gold'])

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print '%s was sent to the penalty box' % self.players[self.current_player]['name']
        self.players[self.current_player]['in_penalty_box'] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.players[self.current_player]['gold'] == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break
