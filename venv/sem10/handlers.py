import os.path
import pickle
import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


(
    OP_BUTTON_STATE,  # 0
    OP_INPUT_STATE,
    NUM_A_STATE,      # 1 ...
    NUM_B_STATE,
) = range(4)  # [0, 1, 2, ..]
r: complex = 3+2j

def save_data(data, id):
    with open(f'{id}.pickle', 'wb') as f:
        pickle.dump(data, f)


def load_data(id):
    file_name = f'{id}.pickle'
    if not os.path.exists(file_name):
        return None

    with open(file_name, 'rb') as f:
        return pickle.load(f)



def op_select_handler(update: Update, context: CallbackContext) -> int:
    # сохранить с какими числами работаем (с вещественными или целыми)
    text = update.message.text

    data = load_data(update.effective_user.id)
    if not data:
        data = {
            "username": update.effective_user.username,
            "num_a": 0,
            "num_b": 0,
            "op": '',  # +, -, *...
            "num_type": float
        }



    if "R" in text:
        data["num_type"] = float
    elif "C" in text:
        data["num_type"] = complex

    save_data(data, update.effective_user.id)

    # Предложить пользователию выбрать действие InlineKeyboard
    kb = [
        [InlineKeyboardButton("a + b", callback_data="+"), InlineKeyboardButton("a - b", callback_data="-"),
         InlineKeyboardButton("a * b", callback_data="*"), InlineKeyboardButton("a / b", callback_data="/"),
         InlineKeyboardButton("a // b", callback_data="//"), InlineKeyboardButton("a % b", callback_data="%")],
    ]
    reply_kb_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text(f"{data} \nВыберите операцию: ", reply_markup=reply_kb_markup)
    return OP_INPUT_STATE


def op_input_handler(update: Update, context: CallbackContext) -> int:

    data = load_data(update.effective_user.id)

    data["op"] = update.callback_query.data   # +, -
    save_data(data, update.effective_user.id)
    update.callback_query.message.edit_text("Введите число А: ")
    return NUM_A_STATE

def num_a_handler(update: Update, context: CallbackContext) -> int:
    data = load_data(update.effective_user.id)

    data["num_a"] = update.message.text

    save_data(data, update.effective_user.id)

    update.message.reply_text("Введите число Б: ")
    return NUM_B_STATE


def num_b_handler(update: Update, context: CallbackContext) -> int:
    data = load_data(update.effective_user.id)
    data["num_b"] = update.message.text

    # выполнить рассчет и вывести ответ
    num_a = data["num_type"](data["num_a"])
    num_b = data["num_type"](data["num_b"])

    logging.info(f"The values of A and B are {num_a} and {num_b}.")
    try:
        data["result"] = eval(f'{num_a} {data["op"]} {num_b}')
        logging.info(f'A {data["op"]} B successful with result: {num_a} {data["op"]} {num_b}.')
        update.message.reply_text(f"Результат вычислений: {data['result']}")
        save_data(data, update.effective_user.id)
        return ConversationHandler.END
    except ZeroDivisionError as err:
        logging.exception("ZeroDivisionError")
        update.message.reply_text("Деление на ноль запрещено. Попробуйте заново.")
        return ConversationHandler.END