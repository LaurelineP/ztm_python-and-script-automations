""" Manipulating data from a CSV file"""

import csv

from custom_utils import get_curr_dir, log_header

CURRENT_FOLDER = get_curr_dir(__file__)


__desired_headers = [
    'original_title', 'year', 'genre',
    'duration', 'country', 'language',
    'description', 'votes'
]


def interpret_votes(votes_count_str):
    """Interpret in a human friendly way the vote"""
    votes_count = int(votes_count_str)
    if votes_count >= 2000:
        return 'a big deal of people'
    elif votes_count < 2000 and votes_count >= 1000:
        return 'a lot of people'
    elif votes_count < 1000 and votes_count >= 500:
        return 'some people'
    elif votes_count < 500 and votes_count > 0:
        return 'few people'
    else:
        return 'no one'


def manipulate_csv(file_path, file_output, desired_headers=None):
    """
        Manipulate a csv and generate its result - append `_output`in file name
        - original file contained dads jokes
        - here we are working with movies instead
    """
    log_header('manipulate_csv')

    if desired_headers is None:
        desired_headers = __desired_headers

    file_path = f"{CURRENT_FOLDER}/{file_path}"
    file_output_path = f"{CURRENT_FOLDER}/{ file_output }"

    collected_rows = []
    collected_rows.append(desired_headers)

    # ---------------------------------------------------------------------------- #
    #                       READING & MANIPULATE CSV CONTENT                       #
    # ---------------------------------------------------------------------------- #
    with open(file_path, "r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)

        # ---------------------------------- HEADERS --------------------------------- #
        try:
            original_headers = next(csv_reader)
        except StopIteration:
            print('[ csv headers ] - could not get headers')
            original_headers = []

        # ------------------------ VALUES FROM DESIRED HEADERS ------------------------ #
        # Loops over the desired headers amongst the file headers to collect desired data

        # Loops over csv each line aka row
        for row in csv_reader:
            new_row = []

            # Loops over desired headers ( default or user's )
            for desired_header in desired_headers:
                if desired_header in original_headers:

                    # Retrieve the original csv header to retrieve the value
                    idx = original_headers.index(desired_header)
                    value = row[idx]

                    new_row.append(value)

                    # Special analyse with votes value for a new column
                    if desired_header == 'votes':
                        _interpreted_vote = interpret_votes(value)
                        new_row.insert(idx + 1, _interpreted_vote)

            # Once the row has completed its population, store it
            collected_rows.append(new_row)

    # ---------------------------------------------------------------------------- #
    #                            WRITING IN CSV NEW FILE                           #
    # ---------------------------------------------------------------------------- #
    """
        We could reuse the functions previously defined in others files,
    but we will define it here for practice purposes
    """

    with open(file_output_path, 'w', newline='', encoding='UTF-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(collected_rows)
    print(f'\t --- file output: {file_output_path}')
