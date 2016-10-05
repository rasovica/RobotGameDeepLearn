import rg
import math


class Robot:
    def load(self):

    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def act(self, game):
        # if we're in the center, stay put
        if self.location == rg.CENTER_POINT:
            return ['guard']

        # if there are enemies around, attack them
        num = 0
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    num = num+1
                    if num >3:
                        return['suicide']
                    else:
                        return ['attack', loc]

        # move toward the center
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        pass
