import os
import re
import sys

def CalculateScoreA(games) :
    score = 0
    for game in games:
        opponent, me = (int(x) for x in game.split(' ', 1))

        difference = me - opponent

        if opponent == me:
            score += 3 
        elif difference % 3 == 1:
            score += 6

        score += me

    return score

def CalculateScoreB(games) :
    score = 0
    for game in games:
        opponent, desired_outcome = (int(x) for x in game.split(' ', 1))

        if desired_outcome == 1:
            score += ((opponent + 1) % 3) + 1
        elif desired_outcome == 2:
            score += 3
            score += opponent
        elif desired_outcome == 3:
            score += (opponent % 3) + 1
            score += 6

    return score

games = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split('\n')
        if line:
            games.append(line[0])

games = [re.sub("A|X", "1", a) for a in games]
games = [re.sub("B|Y", "2", a) for a in games]
games = [re.sub("C|Z", "3", a) for a in games]

resultA = CalculateScoreA(games)
resultB = CalculateScoreB(games)

print("Result A: ", resultA)
print("Result B: ", resultB)