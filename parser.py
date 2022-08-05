# ISO-code города, для которого выбираем данные
MOSCOW = 'RU-MOW'
SAINT_PETERSBURG = 'RU-SPE'


def parser(data: dict) -> dict | None:
    """
    Парсинг одного продукта.
    :param data: Словарь со всеми данными по одному товару
    """
    regions = (data.get('available')
               .get('offline')
               .get('region_iso_codes', []))
    if MOSCOW in regions or SAINT_PETERSBURG in regions:
        product_data = {
            'ID': data.get('id'),
            'title': data.get('title'),
            'url': data.get('link').get('web_url')
        }
        old_price = data.get('old_price')
        if old_price:
            product_data['price'] = old_price.get('price')
            product_data['promo_price'] = data.get('price').get('price')
        else:
            product_data['price'] = data.get('price').get('price')

        return product_data
