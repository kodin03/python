from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
import random

game_data = {"candies": 2021, "player": 1}
m = 28


def input_player_name_handler(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    game_data["player"] = name

    count = random.randint(0, 1)
    if game_data["candies"] % 10 == 1 and 9 > game_data["candies"] > 10:
        letter = 'а'
    elif 1 < game_data["candies"] % 10 < 5 and 9 > game_data["candies"] > 10:
        letter = 'ы'
    else:
        letter = ''
    while game_data["candies"] > 0:
        if not count % 2:
            move = random.randint(1, m)
            print(f'Я забираю {move}')
        else:
            print(f'{game_data["player"][1]}, Ваш ход')
            move = int(input())
            if move > n or move > m:
                print(
                    f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if n >= move <= m:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


def input_player_age_handler(update: Update, context: CallbackContext) -> int:
    age = update.message.text
    if not age.isdigit():
        update.message.reply_text(f"Ошибка! Введите возраст число: ")
        return PLAYER_AGE_STATE

    user_profile["age"] = int(age)

    reply_kb_markup = ReplyKeyboardMarkup([
        ["М", "Ж"],
    ], one_time_keyboard=True)

    update.message.reply_text(f"Введите пол:", reply_markup=reply_kb_markup)

    return PLAYER_GENDER_STATE


def input_player_gender_handler(update: Update, context: CallbackContext) -> int:
    user_profile["gender"] = update.message.text

    update.message.reply_text(f"Вы ввели следующую информацию: {user_profile}")
    return ConversationHandler.END

