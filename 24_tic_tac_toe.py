icons = {
  'player 1': 'X',
  'player 2': 'O'
}

boards = [' ' for i in range(9)]

def print_board():
  row_1 = '|'.join(boards[0:3])
  row_2 = '|'.join(boards[3:6])
  row_3 = '|'.join(boards[6:9])
  print(row_1)
  print(row_2)
  print(row_3)

def player_move(player, pos):
  icon = icons[player]
  if boards[pos - 1] != ' ':
    print('That place has already been taken')
    return False
  boards[pos - 1] = icon
  return True

def is_winning(player):
  icon = icons[player]
  if boards[0] == icon and boards[1] == icon and boards[2] == icon or \
    boards[3] == icon and boards[4] == icon and boards[5] == icon or \
    boards[6] == icon and boards[7] == icon and boards[8] == icon or \
    boards[0] == icon and boards[3] == icon and boards[6] == icon or \
    boards[1] == icon and boards[4] == icon and boards[7] == icon or \
    boards[2] == icon and boards[5] == icon and boards[8] == icon or \
    boards[0] == icon and boards[4] == icon and boards[8] == icon or \
    boards[2] == icon and boards[4] == icon and boards[6] == icon:
    return True
  return False

step = 0
players = list(icons.keys())
print_board()
while step < 9:
  player = players[step % 2]
  pos = int(input('Your turn {}: '.format(player)).strip())
  if (player_move(player, pos)):
    print_board()
    if is_winning(player):
      print('Congratulation {}, you win the match'.format(player))
      break
  else:
    step -= 1

  step += 1

  if (step == 9):
    print('The game is draw')
    break
