import csv
from scrapingbee import ScrapingBeeClient


MOSCOW = 'RU-MOW'
SAINT_PETERSBURG = 'RU-SPE'

with open('result.csv', 'w', newline='') as file:
    columns = [
        'ID',
        'title',
        'price',
        'promo_price',
        'url',
    ]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    client = ScrapingBeeClient(api_key='2C5XGSNI2OQB9LGFE61XZK5928HJOSXOAO5E6DJR915SFT0K3X6P8UT8Y5X4JDCKVFD25967N26ANYYO')
    offset = 0
    while True:
        url = 'https://api.detmir.ru/v2/products?filter=categories[]' \
              '.alias:zdorovyj_perekus_pp;promo:false;withregion:' \
              'RU-MOW&expand=meta.facet.ages.adults,meta.facet.gender.' \
              f'adults,webp&meta=*&limit=100&offset={offset}'
        response = client.get(url=url)
        data = response.json().get('items')
        if not data:
            break
        else:
            for product in data:
                regions = product.get('available').get('offline').get('region_iso_codes', [])
                if MOSCOW in regions or SAINT_PETERSBURG in regions:
                    product_data = {
                        'ID': product.get('id'),
                        'title': product.get('title'),
                        'url': product.get('link').get('web_url')
                    }
                    old_price = product.get('old_price')
                    if old_price:
                        product_data['price'] = old_price.get('price')
                        product_data['promo_price'] = product.get('price').get('price')
                    else:
                        product_data['price'] = product.get('price').get('price')

                    writer.writerow(product_data)

            offset += 30
