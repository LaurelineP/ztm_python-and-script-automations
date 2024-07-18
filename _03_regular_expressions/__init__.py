"""
    Regular Expressions
"""
import re
from datetime import datetime

from custom_utils import log, log_header

print('\n\n\n')
log_header('03. Regular Expression', False)
print(' --- cleaning folder and files')
print('\n\n\n')


def explore_search():
    """Using "search" method """
    
    log('Regular Expression - explore_search')

    # searching a word
    text = 'This is the way we do progress,\n\t by doing mistakes and solving them.'
    matched = re.search('progress', text).group()
    print(f'Text 1 - searching for plain text:\n\t"{text}"')
    print('\t> Regexp value: "progress"')
    print(f'\t> Matched: "{matched}"\n')

    # searching for group
    text = 'This is the 12th anniversary'
    matched = re.search('\d{1,2}[a-z]{2}', text).group()
    print(f'\nText 2 - searching for a group:\n\t "{text}"')
    print('\t> Regexp value: "\d{1,2}[a-z]{2}"')
    print(f'\t> Matched: "{matched}"\n')


    # searching for group - using regexp string and indexed of group
    today = datetime.today().strftime('%B %d, %Y')
    text = f'Your order will arrive today: {today}'
    regxp = r'(\w+) (\d{1,2}), (\d{4})'
    matched = re.search(regxp, text).group()
    matched1 = re.search(regxp, text).group(1)
    matched2 = re.search(regxp, text).group(2)
    matched3 = re.search(regxp, text).group(3)
    print(f'\nText 3 - searching for a group and group indexes:\n\t "{text}"')
    print(f'\t> Regexp value: "{regxp}"')
    print(f'\t> Matched: "{matched}"')
    print(f'\t> Matched group 1: "{matched1}"')
    print(f'\t> Matched group 2: "{matched2}"')
    print(f'\t> Matched group 3: "{matched3}"\n')


def explore_findall():
     """Using "findall" method """
     log('Regular Expression - explore_findall')

    # searching for all same pattern - here year
     text = "The early years of computing,\ 1945 and 1950, laid the groundwork for modern informatics. Subsequent milestones in 1969, the birth of the internet, and 1983, the introduction of DNS, further shaped the field. The advent of the World Wide Web in 1991 revolutionized information sharing and consumption."
     regxp = r'\d{4}'
     matched = re.findall(regxp, text)
     print(f'\nText 1 - searching for a group and group indexes:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Matched: "{matched}"')


def explore_sub():
     """Using "sub" method """
     log('Regular Expression - explore_findall')

    # replacing pattern w/ substituted value - email patterns
     text = "Contact us at support@example.com or info@example.com"
     regxp = r'\w+@\w+\.\w{1,3}'
     substitution = "<email>"
     substituted = re.sub(regxp, substitution, text)
     print(f'\nText 1 - replacing found pattern by a text:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Substitution: "{substitution}"')
     print(f'\t> Substituted: "{substituted}"')

     # replacing pattern, using group and group manipulation
     text = "JavaScript has seen significant milestones over the last few years. Notably, the release of ECMAScript 6 on 2015-06-17 introduced a new syntax and features. The introduction of async/await in ECMAScript 2017, officially published on 2017-06-08, marked a major advancement in asynchronous programming. More recently, the ECMAScript 2020 specification, finalized on 2020-06-16, brought optional chaining and nullish coalescing among other features."
     regxp = r'(\d{4})-(\d{2})-(\d{2})'
     substitution = r"\2/\3/\1"
     substituted = re.sub(regxp, substitution, text)
     print(f'\nText 2 - replacing and group manipulated:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Substitution: "{substitution}"')
     print(f'\t> Substituted: "{substituted}"\n')


def mask_project():
     """SSN Masker Mini Project ( Social Security Number )
        Write a function converting:
            > "123-45-6789"
            > to "***-**-6789"
    Personal implementation 
     """
     
     regxp = r"\d{3}-\d{2}-(\d{4})$"
     instruction = "Please refer your SSN: "

     text = ''
     while not re.match(regxp, text):
          text = input(instruction)



     substitution = r"***-**-\1"
     substituted = re.sub(regxp, substitution, text)
     print(f'\nText 1 - mini project replacing all but last number group:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Substitution: "{substitution}"')
     print(f'\t> Substituted: "{substituted}"')



def explore_alternation():
     """Alternation or OR in Regexp"""
     log('Regular Expression - explore_alternation')

    # multiple choices ( with cases ignore )
     text = "I love cats and DOGS."
     regxp = r"(cat.|dog.)"
     matches = re.findall(regxp, text, re.IGNORECASE)
     print(f'\nText 1 - Alternation multiple choices:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Matches: "{matches}"\n')

    # case sensitive
     text = "Python and PYTHON but Python."
     regxp = r"python"
     matches = re.findall(regxp, text, re.IGNORECASE)
     print(f'\nText 2 - Alternation case sensitive:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Found: "{matches}"\n')

def explore_compilation_flags():
     """Compilation flags ( start "^", end "$" )"""
     log('Regular Expression - explore_compilation_flags')

    # case sensitive + multiline
     text = '''
Python are animals.
But this also refers to Python the programming language.
Python name for the programming language comes 
from Monty Python fans developers.
    '''
     regxp = r"^python"
     matches = re.findall(regxp, text)
     print(f'\nText 1 - Compilation flags with no alternation:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Regexp flag: "re.IGNORECASE"')
     print(f'\t> Found: "{matches}"\n')

     matches = re.findall( regxp, text, re.IGNORECASE | re.MULTILINE )
     print(f'\nText 2 - Compilation flags with alternation:\n\t "{text}"')
     print(f'\t> Regexp value: "{regxp}"')
     print(f'\t> Regexp flag: "re.IGNORECASE" | "re.MULTILINE"')
     print(f'\t> Found: "{matches}"\n')