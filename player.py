def get_area(s):
    area = [['X', '.', '.', '.'],
            ['.', 'o', '.', '.'],
            ['.', '.', '.', 'o'],
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
            if nowy <= area_len-2:
                try:
                    if not area[nowy+1][nowx] == 'o':
                        nowy += 1
                        area[nowy][nowx] = 'X'
                        area[nowy-1][nowx] = '.'

                except:
                    print('Вы дошли до края платформы!')


        elif where == "вверх" or where == 'w':
            if nowy >= area_len-3:
                try:

                    if not area[nowy-1][nowx] == 'o':
                        nowy -= 1
                        area[nowy][nowx] = 'X'
                        area[nowy+1][nowx] = '.'
                    else:
                        print('Тут стена :|')

                except:
                    print('Вы дошли до края платформы!')


        elif where == "право" or where == 'd':
            if nowx <= area_len-2:
                try:

                    if not area[nowy][nowx+1] == 'o':
                        nowx += 1
                        area[nowy][nowx] = 'X'
                        area[nowy][nowx-1] = '.'

                except:
                    print('Вы дошли до края платформы!')


        elif where == "лево" or where == "a":
            if nowx >= area_len-3:
                try:
                    if not area[nowy][nowx-1] == 'o':
                        nowx -= 1
                        area[nowy][nowx] = 'X'
                        area[nowy][nowx+1] = '.'

                except:
                    print('Вы дошли до края платформы!')

        print_map(area)


game(get_area(4))
