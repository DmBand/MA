```Python 3.10```

## Запуск парсера
### 1. Если сайт [detmir.ru](https://detmir.ru/) доступен без прокси:
Выполните: ```pip install requests```

Запустите файл ```main.py```

### 2. Если сайт [detmir.ru](https://detmir.ru/) не доступен:
Выполните: ```pip install scrapingbee```

Воспользуйтесь бесплатным пробным ключом из файла ```SECRET.py```,
изменив файл ```main.py``` следующим образом:

<pre>
from writter import executor, info_decorator
from SECRET import API_KEY


@info_decorator
def main():
    executor(filename='result', api_key=API_KEY)


if __name__ == '__main__':
    main()
</pre>
#### У ключа API_KEY ограниченно количество бесплатных использований!

Запустите файл ```main.py```
