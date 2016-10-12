import rg
import math
import random

all_locs = [(x, y) for x in xrange(19) for y in xrange(19)]
# set of all spawn locations
all_locs = {loc for loc in all_locs if 'invalid' not in rg.loc_types(loc)}


class Robot:
    def __init__(self):
        self.weight = list()

    def load(self, game):
        with open("weights", "r+") as file:
            line = file.readline()
            for a in line.split(","):
                self.weight.append(a)

    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    def act(self, game):
        self.load(game)

        print self.weight
        pass
