import random
import re
from faker import Faker
import argparse
import json
import csv

TITLES = 'titles'
AUTHORS = 'authors.txt'


def conf_py():
    """
    Считывает строку из файла conf.py
    :return: возвращает сроку
    """
    with open('conf.py', 'rt', encoding='utf8') as a:
        model = a.readline()
        print(model)
    return model


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
    patt_reg = re.compile(r'\b[А-Я]\w+\b\s\b[А-Я]\w+\b', re.DOTALL)
    with open("authors.txt", 'rt', encoding='utf8') as file:
        a = []
        data = patt_reg.findall(file.read())
        for i in range(5):
            a.append(random.choice(data).strip())
        if data is None:
            print(ValueError)

        result = random.choice(data).strip()
        print(result)
        return a


def random_year():
    """

    :return: возвращает случаный год в указанном промежутке
    """
    res = random.randint(1999, 2020)
    print(res)
    return res


def random_pages():
    """
    Генерирует страницы
    :return: возвращает случаную страницу в указанном промежутке
    """
    res = random.randint(1, 200)
    print(res)
    return res


def random_isbn13():
    """
    Генерирует isbn13 код
    :return: возвращает случаный isbn13 код
    """
    fake = Faker()
    Faker.seed(0)
    for i in range(5):
        fake.isbn13()
    res = fake.isbn13()
    return res


def random_rating():
    """
    Генерирует рейтинг
    :return: возвращает рейтинг в пределах от 0 до 5
    """
    res = int(random.uniform(0, 5))
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
    res = int(random.randint(1, 100))
    print(res)
    return res


def random_book(pk: int = 1):
    while True:
        model = conf_py()
        pk = pk
        title = random_title()
        year = random_year()
        pages = random_pages()
        isbn13 = random_isbn13()
        rating = random_rating()
        price = random_price()
        discount = random_discount()
        author = random_authors()
        one_book = {
            "model": model,
            "pk": pk,
            "fields": {
                "title": title,
                "year": year,
                "pages": pages,
                "isbn13": isbn13,
                "rating": rating,
                "price": price,
                "discount": discount,
                "author": author

            }
        }
        yield one_book
        pk += 1


def countee():
    count = 10
    pk = 0
    for i in random_book():
        pk += 1
        print(i)
        print(f'Функция {random_book} была вызвана {pk} раз(а)')
        if pk == count:
            break


def create_output_format(args):
    args.output_format = 'output_format'
    if args.output_format == 'json':
        get_json_file()
    if args.output_format == 'csv':
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

    return parser


def get_json_file():
    with open('ty.json', "w") as fl:
        json.dumps(fl, indent=4)


def get_csv_file():
    with open('ty.csv', "w") as fk:
        csv.DictReader(fk, delimiter=',')


if __name__ == '__main__':
    random_book()
    print(next(random_book()))
    countee()
