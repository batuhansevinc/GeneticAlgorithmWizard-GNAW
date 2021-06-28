import random


def fitness(ind):
  avg_f = 0  # average fitness
  for a1 in range(0, 200):
    f = 0  # fitness for current board
    b = [[random.randint(0,1) for i in range(0, 10)] for x in range(0, 10)]
    x, y = 0, 0   # x and y on the board, initially zero
    for a2 in range(0, 200):
      # find the combination:
      # N-S-W-E-C  -> (00100)_3 -> 9
      comb = 0
      comb += b[x][y]  # 3^0 - just take the value
      if x+1 == 10:  # wall
        comb += pow(3,1) * 2   # 3^1 - wall
      else:
        comb += pow(3,1) * b[x][y]
      if x-1 < 0:
        comb += pow(3,2) * 2
      else:
        comb += pow(3,2) * b[x][y]
      if y+1 == 10:
        comb += pow(3,3) * 2
      else:
        comb += pow(3,3) * b[x][y]
      if y-1 < 0:
        comb += pow(3,4) * 2
      else:
        comb += pow(3,4) * b[x][y]
      # 0 -> do nothing, 1 -> go left, 2 -> go right, 3 -> go up, 4 -> go down
      # 5 -> pick up, 6 -> go random
      # skipping 0 since it does nothing...
      action = ind[comb]
      if action == 6:
        # go random, so set action randomly between 1 and 4
        action = random.choice(range(1,5))  # 5 -> exclusive...
      if action == 1:
        # go left
        if x-1 < 0:
          f -= 1  # fine 1 points? update these as required...
        else:
          x -= 1  # update x so it moves left.
      elif action == 2:
        # go right
        if x+1 == 10:
          f -= 1
        else:
          x += 1
      elif action == 3:
        # go up
        if y-1 < 0:
          f -= 1
        else:
          y -= 1
      elif action == 4:
        if y+1 == 10:
          f -= 1
        else:
          y += 1
      elif action == 5:    # pick up can
        if b[x][y] == 1:   # there is a soda can
          b[x][y] = 0      # update board, pick it up (combination changes)
          f += 10
        else:
          f -= 5
      # repeat until 200 are done
    avg_f += f
  return avg_f / 200