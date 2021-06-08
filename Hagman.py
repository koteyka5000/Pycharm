def welcome_speech(t):
    print(f"""
    Добро пожаловать в игру!
    Ваша задача - угадать слово за несколько попыток,
    иначе Вы проиграете! :(
    загаданное слово состоит из {len(t)} букв
    """)


def start_template(w):
    t = []
    for l in w:
        t.append('_')
    return t


def list_to_string_convert(t):
    s = ''
    return s.join(t)


def get_word(w):
    return w[0]


def replace(inp, word, template):
    for i in range(len(word)):
        if inp == word[i]:
            template[i] = inp
    return template

def game():
    progress = True
    word = ['oreaenegeeeg']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        print('======================')
        print(f'У вас осталось попыток: {lifes}')
        print(f'Сейчас слово: {list_to_string_convert(template)}')
        inp = input('Введите предпологаемую букву: ')
        if inp in word_in_play:
            template = replace(inp, word_in_play, template)
        else:
            print('Такой буквы в слове нет :(')
            lifes -= 1
        if lifes == 0 or word_in_play == template:
            progress = False
    if lifes == 0:
        print(f'Вы хорошо держались :)\nЗагаданым словом было {word_in_play}')
    elif word_in_play == template:
        print(f'Вы победили!! :)\nУ вас осталось попыток: {lifes}')
game()
