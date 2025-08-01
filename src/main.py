import logging
import platform
import random
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())


# 1 - easy(4)
# 2 - med(5)
# 3 - hard(6)
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

def show_word_state(word, guessed):
    display = [letter if letter in game_status['right_letters'] else '_' for letter in word]
    print("Текущее слово:", " ".join(display))
    return '_' not in display

def choose_difficulty():
    print("Выберите сложность(1,2,3)")
    dif = int(input())
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
    is_win = show_word_state(word, game_status)
    if is_win:
        return True
    print(HANGMAN_PICS[game_status['attemps']])
    letter: str = input('Введите букву\n').lower()
    if len(letter) != 1:
        print('введите 1 букву')
        pass
    else:
        if letter in word:
            print('верно')
            game_status['right_letters'].add(letter)
        elif letter in game_status['right_letters']:
            print('вы уже пробовали эту букву')
        else:
            print('неверно')
            game_status['attemps'] -= 1
            print(f'Осталось {game_status['attemps']} попыток')
if __name__ == "__main__":
    dif, word = choose_difficulty()
    while game_status['attemps'] != 0:
        if letter_answer(word, game_status):
            print('Победа')
            break
    else:
        print('вы проиграли')
