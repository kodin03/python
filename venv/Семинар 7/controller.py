

from view import render_template

from model import User, Phone



def default_controller(data=None, cls=True):
    """Default controller"""
    render_template(context={}, template="default", cls=cls)
    return (input(), None)


def exit_controller(data=None, cls=True):
    render_template(context={}, template="exit", cls=cls)
    exit()


def all_users_controller(data=None, cls=True):
    users = User.all()
    render_template(context={'users':users}, template="all_users", cls=cls)
    input("Продолжить?")
    return 'main', None # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user # (next state, data)


def add_user_controller(data=None, cls=True):
    render_template(context={}, template="add_user", cls=cls)
    username = input()
    user = User.add(username)
    return 21, user # (next state, data)


def add_phone_controller(user, cls=True):
    render_template(context={}, template="add_phone", cls=cls)
    phone_number = input()
    phone = Phone.add(phone_number, user)
    return 212, user # (next state, data)


def add_more_controller(user, cls=True):
    render_template(context={}, template="add_more", cls=cls)
    answer = input()
    if answer == 'Y':
        return 21, user
    return 51, user # (next state, data)

def get_controller(state):
    return controller_dict.get(state, default_controller)


controller_dict = { # use dict type instead of if else chain
    '0': exit_controller,
    '1': all_users_controller,
    '2': add_user_controller,
    21: add_phone_controller, # user can't enter 21 of int type
    212: add_more_controller
}