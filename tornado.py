import time
from cryptography.fernet import Fernet
import art
from bs4 import BeautifulSoup
import requests
import os

art.tprint("TORNADO")
def checking_for_updates():
    try:
        response = requests.get('https://1mteapp.github.io/tornado_download/version')
        soup = BeautifulSoup(response.text, "html.parser")
        check = soup.find('h1').get_text()
        if check == '1.1':
            print('У Вас установлена последняя версия!\n')
            time.sleep(2)

            start_start()
        else:
            print('Вышло новое обновление! Скачайте его на нашем официальном сайте - https://1mteapp.github.io/tornado_download/\n')
            time.sleep(2)
            start_start()
    except:
        print('Произошла ошибка при проверке обновления!')
        start_start()

def start_start():
    print("1  -   Расшифровка сообщения.")
    print("2  -   Зашифровка сообщения.")
    print("3  -   Встроенный браузер.")
    input_start()

def decrypt(Fernet):
    key = input("Введите ключ: ")
    f = Fernet(key)
    token = input("Введите токен: ")
    decrypted_text = f.decrypt(token)
    print(f"Расшифровка сообщения:\n{decrypted_text.decode()}")
    start_start()


def encrypt(Fernet):
    key = Fernet.generate_key()
    print("Ваш сгенерированный ключ:")
    print(key.decode())
    f = Fernet(key)
    token = f.encrypt(input("Введите текст для зашифровки: ").encode())
    f.decrypt(token)
    print("Ваш токен:")
    print(token.decode())
    start_start()

def input_start():
    start = input(" Выберите действие:\n")
    if start == "1":
        decrypt(Fernet)
    else:
        if start == "2":
            encrypt(Fernet)
        else:
            if start == "3":
                browser()
            else:
                if start != "1" and "2" and "3":
                    print("Вы ввели неправильное число!\n")
                    time.sleep(2)
                    input_start()

def run_search(query):
    url = f'https://www.bing.com/search?q={query}'
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('li', class_='b_algo')


    for counter, result in enumerate(results):
        title = result.find('h2').text
        link = result.find('a')['href']
        print(f"{counter}. {title} - {link}\n")

    start_start()
def browser():
    run_search(input("Введите запрос поиска:\n").replace(' ', ''))

checking_for_updates()
