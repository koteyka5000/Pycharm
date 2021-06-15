def get_area(s):
    area = [['X', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']]
    return [area, s]


def print_map(area):
    print('==========')
    print(*area[0], '\n', *area[1], '\n', *area[2], '\n', *area[3], sep='')
    print('==========')

def game(areaq):
    area = areaq[0]
    area_len = areaq[1]
    print_map(area)
    nowx = 0
    nowy = 0
    while True:
        where = input('wasd: ')

        if where == "вниз" or where == 's':
            if nowy <= 2:
                try:
                    nowy += 1
                    area[nowy][nowx] = 'X'
                    area[nowy-1][nowx] = '.'

                except:
                    print('Вы дошли до края платформы!')

        elif where == "вверх" or where == 'w':
            if nowy >= 1:
                try:
                    nowy -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy+1][nowx] = '.'

                except:
                    print('Вы дошли до края платформы!')

        elif where == "право" or where == 'd':
            if nowx <= 2:
                try:
                    nowx += 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx-1] = '.'

                except:
                    print('Вы дошли до края платформы!')

        elif where == "лево" or where == "a":
            if nowx >= 1:
                try:
                    nowx -= 1
                    area[nowy][nowx] = 'X'
                    area[nowy][nowx+1] = '.'

                except:
                    print('Вы дошли до края платформы!')

        print_map(area)


game(get_area(4))
