import json
import os
from pprint import pprint

from bs4 import BeautifulSoup
import csv
import requests
import multiprocessing as ml
import re
from Stemmer import Stemmer

main_path = 'data'
data = {
    'авто'       : 'https://site-directory.ru/avto',
    'культура'   : 'https://site-directory.ru/kultura',
    'спорт'      : 'https://site-directory.ru/sport',
    # 'для_взрослых': 'https://site-directory.ru/dlya-vzroslykh',
    'юмор'       : 'https://site-directory.ru/yumor',
    'образование': 'https://site-directory.ru/obrazovanie',
    'бизнес'     : 'https://site-directory.ru/biznes',
    'путешествие': 'https://site-directory.ru/puteshestvie',
}


# soup = BeautifulSoup('')


def text_cleaner(text):
    text = text.lower()  # приведение в lowercase
    stemmer = Stemmer('russian')
    text = ' '.join(stemmer.stemWords(text.split()))
    text = re.sub(r'\b\d+\b', ' digit ', text)  # замена цифр
    return text


def get_data_from_url_js(url: str):
    if url[-1] == '/':
        url = url[:-1]
    dom = url[url.rindex('/') + 1:url.rindex('.')]
    r = requests.get(url)
    if r.status_code != 200:
        return
    soup = BeautifulSoup(r.text, features="html.parser")
    res_data = list(filter(lambda x: x and len(x) >= 3 and 'digit' not in x, map(text_cleaner, soup.get_text('\n').split('\n'))))
    return res_data


def get_data_from_url(tag: str, url: str):
    if 'data' not in os.listdir():
        os.mkdir('data')
    if tag not in os.listdir('data/'):
        os.mkdir(f'data/{tag}')

    try:
        if url[-1] == '/':
            url = url[:-1]
        dom = url[url.rindex('/') + 1:]
        r = requests.get(url)
        if r.status_code != 200:
            return
        soup = BeautifulSoup(r.text, features="html.parser")
        res_data = list(filter(lambda x: x and len(x) >= 3 and 'digit' not in x, map(text_cleaner, soup.get_text('\n').split('\n'))))
        print(f'{url} > {len(res_data)} ::: {main_path}/{tag}/{dom}.txt')
        open(f'{main_path}/{tag}/{dom}.txt', 'w', encoding='utf8').writelines(list(map(lambda x: x + '\n', res_data)))
    except:
        return


def get_data_from_url_soft(args):
    tag, url = args
    if 'data' not in os.listdir():
        os.mkdir('data')
    if tag not in os.listdir('data/'):
        os.mkdir(f'data/{tag}')

    try:
        if url[-1] == '/':
            url = url[:-1]
        dom = url[url.rindex('/') + 1:]
        r = requests.get(url)
        if r.status_code != 200:
            return
        soup = BeautifulSoup(r.text, features="html.parser")
        res_data = list(filter(lambda x: x and len(x) >= 3 and 'digit' not in x, map(text_cleaner, soup.get_text('\n').split('\n'))))
        print(f'{url} > {len(res_data)} ::: {main_path}/{tag}/{dom}.txt')
        open(f'{main_path}/{tag}/{dom}.txt', 'w', encoding='utf8').writelines(list(map(lambda x: x + '\n', res_data)))
    except:
        return


def get_urls(tag):
    r = requests.get(data[tag])
    soup = BeautifulSoup(r.text, features="html.parser")
    for i in soup.find_all('div', class_='views-row')[::2]:
        url = list(filter(lambda x: x, i.text.split('\n')))[-1]
        print(url)
        get_data_from_url(tag, url)


if __name__ == '__main__':
    # urls = []
    # for tag in data.keys():
    #     r = requests.get(data[tag])
    #     soup = BeautifulSoup(r.text, features="html.parser")
    #     for i in soup.find_all('div', class_='views-row')[::2]:
    #         url = list(filter(lambda x: x, i.text.split('\n')))[-1]
    #         print(url)
    #         urls.append([tag, url])
    # with open('data.csv', 'w', encoding='utf8') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(urls)
    # get_urls('путешествие')
    with ml.Pool(7) as p:
        print(p.map(get_urls, data.keys()))