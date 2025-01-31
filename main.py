#!/usr/bin/python3

# Tournament elimination stage calc
# Assume maximal possible results (most competitive case scenario)
# Find top possible binomial distribution of wins/non-wins

import math


# defined Params
totalPlayers = 526
topPlayersQualified = 64
# ptsWin = 7
# ptsDraw = 3
# ptsLose = 0

# derived Params
# there is a maximum score based on max rounds where every player plays up until 1 top player remains
# however there may be 'bonus' players that still need to be matched
# BYE matches occur only on odd-players and count as wins
# We assume greedy, where winners are winning as hard as possible
maxRounds = math.floor( math.log2( totalPlayers ))
extraPlayers = totalPlayers - (2<<(maxRounds - 1))


# binomial distribution of wins / not-wins
type Score = tuple(int, int)    # (wins, non-wins )
type Play = dict[
  "playCount" : int,
  "score"     : Score,
]
type GameDistribution = list[Play] # (distribution of plays)

gameDistribution: GameDistribution = []
for k in range(maxRounds + 1):
  play: Play = {
    "playCount" : math.comb(maxRounds, k),
    "score"     : (maxRounds - k, k),
  }
  # Extra players are all maximal winners. Append them to top
  if(k == 0):
    play["playCount"] += extraPlayers
  gameDistribution.append(play)

# extract top groups
counter = 0
filteredList: gameDistribution = []
for g in gameDistribution:
  if( counter >= topPlayersQualified ):
    break
  counter += g["playCount"]
  filteredList.append(g)
excess = counter - topPlayersQualified

# print results:
print(f'Top {topPlayersQualified} (excess: {excess}):')
[ print(x) for x in filteredList ]
print('Distribution: ')
[ print(x) for x in gameDistribution ]

