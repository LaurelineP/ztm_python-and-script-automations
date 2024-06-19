"""Product Sales Project
- read a logging file stating only product ids daily
- product ids are unique but in this text file it is duplicated

"""

import csv
from datetime import date

from custom_utils import log_header

# Product ID Product Name Unit Price
PRODUCTS_MAPPING = {
    'P001': {'name': 'Wireless Headphones', 'price': 100},
    'P002': {'name': 'Laptop Backpack', 'price': 60},
    'P003': {'name': 'Bluetooth Speaker', 'price': 50},
    'P004': {'name': 'USB Flash Drive', 'price': 20},
    'P005': {'name': 'Mobile Phone Case', 'price': 15},
    'P006': {'name': 'Wireless Mouse', 'price': 30},
    'P007': {'name': 'Laptop Stand', 'price': 40},
    'P008': {'name': 'HDMI Cable', 'price': 15},
    'P009': {'name': 'Smartphone', 'price': 600},
    'P010': {'name': 'External Hard Drive', 'price': 100}
}
HEADERS = ['current_date', 'sales_id', 'product_id', 'product_name', 'price']


def run(input_path, output_path=''):
    """Runs program to generate a readable product sales files"""
    log_header('project: product sales')
    print('--- Processing file...\n')

    with open(input_path, 'r', encoding='UTF-8') as original_file, \
            open(output_path, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(HEADERS)

        sale_id = 1
        original_lines = original_file.read().split('\n')

        for product_id in original_lines:
            sale_id += 1
            row = [
                date.today(),
                sale_id,
                str(product_id),
                PRODUCTS_MAPPING[product_id]['name'],
                PRODUCTS_MAPPING[product_id]['price']
            ]
            csv_writer.writerow(row)

    # ---------------------------------- READING --------------------------------- #
    # input_path = os.path.realpath(f'../{input_path}')
    # with open(input_path, 'r', encoding='UTF-8') as original_file:
    #     lines = original_file.read().split('\n')
    #     print(len(lines))
    # # ----------------------------------- WRITE ---------------------------------- #
    # with open(output_path, 'w', encoding='UTF-8') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow(HEADERS)
    #     sale_id = 1
    #     for product_id in lines:
    #         sale_id += 1
    #         row = [
    #             date.today(),
    #             sale_id,
    #             product_id,
    #             PRODUCTS_MAPPING[product_id]['name'],
    #             PRODUCTS_MAPPING[product_id]['price']
    #         ]
    #         csv_writer.writerow(row)
