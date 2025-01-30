#!/usr/bin/python3

# Tournament elimination stage calc

import math

# defined Params
totalPlayers = 526
topPlayersQualified = 64
ptsWin = 7
ptsDraw = 3
ptsLose = 0

# derived Params
maxRounds = math.ceil( math.log2( totalPlayers ))


# binomial distribution of wins / not-wins
type Score = tuple(int, int)    # (wins, non-wins)
type Play = tuple(int, Score)  # (play count, Score)
type GameDistribution = list[Play] # (distribution of plays)

gameDistribution: GameDistribution = []
for k in range(maxRounds + 1):
  play: Play = ( math.comb(maxRounds, k), (maxRounds - k, k) )
  gameDistribution.append(play)


if( __name__ == "__main__"):
  playSum = 0
  for k, v in enumerate(gameDistribution):
    playSum += v[0]
    print(gameDistribution[k])
  print(playSum)
  pass


