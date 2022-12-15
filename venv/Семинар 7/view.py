
import os
#from jinja2 import Environment, PackageLoader, select_autoescape
"""env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)"""

def screen_cleaner(flag):
    if flag:
        os.system('cls' if os.name == 'nt' else 'clear')


def render_template(context=None, template="", cls=True):
    """Prints rendered template with context data
    Args:
        context (dict, optional): [data for rendering template]. Defaults to None.
        template (str, optional): [template filename]. Defaults to "default.jinja2".
        cls (bool, optional): [Clear screen flas. Shows if screan should be
        cleaned before showing this view]. Defaults to True.
    """


    if not context:
        context = {}
    screen_cleaner(cls)

    if template == "default":
        print("Привет! Это телефонный справочник!\n Что вы хотите сделать?\n 1. Показать все записи\n "
              "2. Создать запись\n 3. Обновить запись\n 4. Удалить запись\n 5. Показать запись\n "
              "0. Выйти из программы\n)")

