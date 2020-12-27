import random
import re
import csv
import argparse
import json

from faker import Faker
import conf


TITLES = 'titles'
AUTHORS = 'authors.txt'


def random_title():
    """
    Генерирует случайное название книги
    :return: возращает случайное название книги из файла title.txt
    """
    with open(TITLES, 'rt', encoding='utf8') as file:
        data = file.readlines()
        result = random.choice(data).strip()
        print(result)

    return result


def random_authors():
    """
    Генерирует случайного автора
    :return: возращает случайного автора из файла authors.txt предварительно проверив регулярными выражениями
    """
    patt_reg = re.compile(r'\b[А-Я]\w+\b\s\b[А-Я]\w+\b')
    with open("authors.txt", 'rt', encoding='utf8') as file:
        a = []
        data = patt_reg.findall(file.read())
        for _ in range(5):
            a.append(random.choice(data).strip())
        if data is None:
            print(ValueError)

        result = random.choice(data).strip()
        print(result)
        return a


def random_year():
    """
    :return: возвращает случайный год в указанном промежутке
    """
    res = random.randint(1999, 2020)
    print(res)
    return res


def random_pages():
    """
    Генерирует страницы
    :return: возвращает случайную страницу в указанном промежутке
    """
    res = random.randint(1, 200)
    print(res)
    return res


def random_isbn13():
    """
    Генерирует isbn13 код
    :return: возвращает случайный isbn13 код
    """
    fake = Faker()
    Faker.seed(0)
    for _ in range(5):
        fake.isbn13()
    res = fake.isbn13()
    return res


def random_rating():
    """
    Генерирует рейтинг
    :return: возвращает рейтинг в пределах от 0 до 5
    """
    res = random.uniform(0, 5)
    print(res)
    return res


def random_price():
    """
    Генерирует цену в пределах
    :return: возвращает цену в пределах от 120 до 5000 рублей
    """
    res = int(random.uniform(1200, 5000))
    print(res)
    return res


def random_discount():
    """
    Генерирует размер скидки, генерируется случайным образом
    :return: возращает размер скидки
    """
    res = random.randint(1, 100)
    print(res)
    return res


def random_book(pk: int = 1):
    count = 5
    model = conf.MODEL
    while True:
        one_book = {
            "model": model,
            "pk": pk,
            "fields": {
                "title": random_title(),
                "year": random_year(),
                "pages": random_pages(),
                "isbn13": random_isbn13(),
                "rating": random_rating(),
                "price": random_price(),
                "discount": random_discount(),
                "author": random_authors()

            }
        }
        yield one_book
        pk += 1
        if pk == count:
            break
        print(f'Функция {random_book} была вызвана {pk} раз(а)')

        # json_str = json.dumps(one_book, indent=4)
        # print(json_str)
        # with open('authors_random', 'w', encoding='utf-8') as f:
        #     f.write(json_str)


def get_json_file(obj, filename, indent=1):
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


def do_output(args):
    # self.json = args.json
    # self.csv = args.csv
    # self.output_format = args.output_format

    if args.output_format == 'output_json':
        get_json_file(one_book, 'tmp_json_indent_4')
    if args.output_format == 'output_csv':
        get_csv_file()


def create_subparsers():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='output_format')

    json_parser = subparsers.add_parser('json')
    json_parser.add_argument('-json', '--index', dest='output format', required=True, type=argparse.FileType('w'),
                             help='if we want parse to json format')

    csv_parser = subparsers.add_parser('csv')
    csv_parser.add_argument('-csv', '--index', dest='output format', required=True,
                            help='if we want parse to csv format')
    args = parser.parse_args()
    return args


def get_csv_file():
    with open('ty.csv', "w") as fk:
        csv.DictReader(fk, delimiter=',')


if __name__ == '__main__':
    one_book = {
        "model": conf.MODEL,
        "pk": 1,
        "fields": {
            "title": random_title(),
            "year": random_year(),
            "pages": random_pages(),
            "isbn13": random_isbn13(),
            "rating": random_rating(),
            "price": random_price(),
            "discount": random_discount(),
            "author": random_authors(),
        }}
    random_book()
    for i in random_book():
        print(next(random_book()))
    print(next(random_book()))
    get_json_file(one_book, 'tmp_json_indent_4')
