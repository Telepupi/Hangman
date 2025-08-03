import random

words_1 = [
"план", "глаз", "боль", "мама", "день"
]
words_2 = [
"книга", "столб", "зверь", "точка", "весна"
]
words_3 = [
"письмо", "акцент", "кнопка", "машина", "платок"
]

game_status= {
    'right_letters': set(),
    'attemps': 6,
}
HANGMAN_PICS = [
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

def choose_difficulty():
    while True:
        try:
            dif = int(input('Выберите сложность(1,2,3)\n'))
            if dif not in (1, 2, 3):
                continue
            break
        except ValueError :
            print('Введите число\n')
    match dif:
        case 1:
            print('слово загадано, ваша сложность - легкая')
            word = random.choice(words_1)
        case 2:
            print('слово загадано, ваша сложность - средняя')
            word = random.choice(words_2)
        case 3:
            print('слово загадано, ваша сложность - сложная')
            word = random.choice(words_3)
        case _:
            print('неверный ввод')
    return dif, word

def letter_answer(word, game_status):
    is_win = show_word_state(word)
    if is_win:
        return True
    print(HANGMAN_PICS[game_status['attemps']])
    letter: str = input('Введите букву\n').lower()
    if len(letter) != 1:
        print('введите 1 букву')
        pass
    else:
        if letter in word:
            print('вы уже пробовали эту букву')
        elif letter in game_status['right_letters']:
            print('верно')
            game_status['right_letters'].add(letter)
        else:
            print('неверно')
            game_status['attemps'] -= 1
            print(f'Осталось {game_status['attemps']} попыток')

def show_word_state(word):
    display = [letter if letter in game_status['right_letters'] else '_' for letter in word]
    print("Текущее слово:", " ".join(display))
    return '_' not in display