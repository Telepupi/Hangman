import myLogging
import game_logic

myLogging.main()

if __name__ == "__main__":
    dif, word = game_logic.choose_difficulty()
    while game_logic.game_status['attemps'] != 0:
        if game_logic.letter_answer(word, game_logic.game_status):
            print('Победа')
            break
    else:
        print('вы проиграли')
