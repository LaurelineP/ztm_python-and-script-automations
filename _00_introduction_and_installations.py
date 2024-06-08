from datetime import datetime

from custom_utils import log_header

print('\n\n\n')
log_header('00. Introduction & Installations', False)
print(' --- prompt_user: ask for interaction ')
print(' --- play_with_text: prints text where case changes ')
print(' --- state_date_difference: prompt for a date - returns how many days it was or remains ')
print('\n\n\n')


# Prompting
# Feeding the script with the user interaction
def prompt_user():
    "Shows the ability to prompt and wait for the user interaction"
    text = 'Please answer the following questions...'
    print(text)

    user_name = input('What is your name ? ')
    user_age = int(input('How old are you ? '))
    print(f'Your name is {user_name} and you are {user_age}')


# Playing with string text methods
def play_with_text(text="Hello World!"):
    "Prints text transformation ( upper | lower case )"
    upper_text = text.upper()
    print(upper_text)

    lower_text = text.lower()
    print(lower_text)


# ---------------------------------------------------------------------------- #
#                                   COMMENTS                                   #
# ---------------------------------------------------------------------------- #
# This is a single line comment
"""
This is a multi line comment
"""

# ---------------------------------------------------------------------------- #
#                         INSTALLATIONS & PYCHARM                              #
# ---------------------------------------------------------------------------- #


date_format = '%Y/%m/%d'


def format_date_y_m_d(datetime_value):
    """[ extra ] From datetime object, get the formatted date string as [ YYYY/MM/DD ]"""
    return datetime_value.strftime(date_format)


def state_date_difference():
    """ [ logic deviation ]  From a given date, it will output how many days it was or remaining days until a point"""
    current_date_string_y_m_d = format_date_y_m_d(datetime.now())

    # Gets date to get the delta with
    requested_date_string_y_m_d = input(
        'Please enter the date [ YYYY/MM/DD ]: '
    )

    # Convert date string to date object
    current_date = datetime.strptime(current_date_string_y_m_d, date_format)
    other_date = datetime.strptime(requested_date_string_y_m_d, date_format)

    # Determine dates position in operation
    is_future_date = other_date > current_date

    days_amount = other_date - current_date if is_future_date else current_date - other_date

    # Conditional return message related to result delta ( past or future )
    sentence_start = 'It remains' if is_future_date else 'It was'
    sentence_end = f'days until {requested_date_string_y_m_d}' if is_future_date else 'days ago'

    return f'{sentence_start} {days_amount.days} {sentence_end}.'
