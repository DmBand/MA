import csv

import requests
from scrapingbee import ScrapingBeeClient

from parser import parser


def executor(filename: str, api_key: str = None) -> None:
    """
    Получает данные из запроса и записывает распаршенные данные в csv-файл.
    :param filename: Название конечного файла с результатами парсинга.
    :param api_key: Если передан, то будет использовано прокси
    и библиотека ScrapingBeeClient.
    """

    with open(f'{filename}.csv', 'w', newline='') as file:
        columns = [
            'ID',
            'title',
            'price',
            'promo_price',
            'url',
        ]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        client = ScrapingBeeClient(api_key=api_key) if api_key else None
        offset = 0
        while True:
            url = 'https://api.detmir.ru/v2/products?filter=categories[]' \
                  '.alias:zdorovyj_perekus_pp;promo:false;withregion:' \
                  'RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.' \
                  f'adults,webp&meta=*&limit=100&offset={offset}'
            if client:
                response = client.get(url=url)
            else:
                response = requests.get(url=url)
            data = response.json().get('items')
            if not data:
                break
            for product in data:
                product_data = parser(data=product)
                if product_data:
                    writer.writerow(product_data)
            offset += 100


def info_decorator(func):
    """ Выводит информацию о начале и конце работы функции """
    def wrapper():
        print('Пожалуйста, подождите... Идет сбор данных.')
        func()
        print('Сбор данных окончен!')
    return wrapper
