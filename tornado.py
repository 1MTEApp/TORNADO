import sys
import time
from cryptography.fernet import Fernet
import art
from bs4 import BeautifulSoup
import requests
import os
import webbrowser

class TornadoApp:
    def __init__(self):
        self.show_banner()
        self.main_menu()

    def show_banner(self):
        try:
            with open('program_name.txt', 'r') as file:
                content = file.read().strip()
                if content:
                    art.tprint(content)
                else:
                    art.tprint("TORNADO")
        except FileNotFoundError:
            art.tprint("TORNADO")

    def main_menu(self):
        while True:
            print("\n" + "="*30)
            print("Главное меню".center(30))
            print("="*30)
            print("1. Расшифровать сообщение")
            print("2. Зашифровать сообщение")
            print("3. Поиск в интернете")
            print("4. Настройки")
            print("5. Выход")
            
            choice = input("\nВыберите действие: ")
            
            if choice == "1":
                self.decrypt()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.web_search()
            elif choice == "4":
                self.settings()
            elif choice == "5":
                print("Завершение работы...")
                time.sleep(1)
                sys.exit()
            else:
                print("Некорректный ввод! Пожалуйста, выберите действие от 1 до 5")

    def decrypt(self):
        print("\n" + "="*30)
        print("Расшифровка сообщения".center(30))
        print("="*30)
        
        try:
            key = input("Введите ключ: ").encode()
            token = input("Введите токен: ").encode()
            
            f = Fernet(key)
            decrypted_text = f.decrypt(token)
            
            print("\nРезультат расшифровки:")
            print("-"*30)
            print(decrypted_text.decode())
            print("-"*30)
        except Exception as e:
            print(f"\nОшибка расшифровки: {str(e)}")

    def encrypt(self):
        print("\n" + "="*30)
        print("Шифрование сообщения".center(30))
        print("="*30)
        
        try:
            text = input("Введите текст для шифрования: ").encode()
            
            key = Fernet.generate_key()
            f = Fernet(key)
            token = f.encrypt(text)
            
            print("\nВаш ключ (сохраните в безопасном месте!):")
            print("-"*30)
            print(key.decode())
            print("-"*30)
            
            print("\nВаш токен:")
            print("-"*30)
            print(token.decode())
            print("-"*30)
        except Exception as e:
            print(f"\nОшибка шифрования: {str(e)}")

    def web_search(self):
        print("\n" + "="*30)
        print("Поиск в интернете".center(30))
        print("="*30)
        
        query = input("Введите поисковый запрос: ").strip()
        if not query:
            print("Запрос не может быть пустым!")
            return
            
        try:
            url = f'https://www.bing.com/search?q={query.replace(" ", "+")}'
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('li', class_='b_algo')
            
            print(f"\nРезультаты поиска для '{query}':")
            print("-"*50)
            
            for idx, result in enumerate(results[:5], 1):
                title = result.find('h2').get_text(strip=True)
                link = result.find('a')['href']
                snippet = result.find('p').get_text(strip=True) if result.find('p') else ""
                
                print(f"\n{idx}. {title}")
                print(f"   {link}")
                print(f"   {snippet[:100]}...")
            
            print("\n0. Возврат в меню")
            choice = input("\nВыберите результат для открытия (1-5) или 0 для отмены: ")
            
            if choice.isdigit() and 1 <= int(choice) <= min(5, len(results)):
                webbrowser.open(results[int(choice)-1].find('a')['href'])
        except Exception as e:
            print(f"Ошибка поиска: {str(e)}")

    def settings(self):
        while True:
            print("\n" + "="*30)
            print("Настройки".center(30))
            print("="*30)
            print("1. Изменить имя программы")
            print("2. Показать текущее имя")
            print("3. Сбросить настройки")
            print("4. Возврат в главное меню")
            
            choice = input("\nВыберите действие: ")
            
            if choice == "1":
                new_name = input("Введите новое имя программы: ")
                with open('program_name.txt', 'w') as file:
                    file.write(new_name)
                print(f"Имя успешно изменено на '{new_name}'!")
            elif choice == "2":
                try:
                    with open('program_name.txt', 'r') as file:
                        print(f"\nТекущее имя: {file.read()}")
                except FileNotFoundError:
                    print("\nТекущее имя: TORNADO (по умолчанию)")
            elif choice == "3":
                try:
                    os.remove('program_name.txt')
                    print("Настройки сброшены к значениям по умолчанию!")
                except FileNotFoundError:
                    print("Настройки уже установлены по умолчанию!")
            elif choice == "4":
                return
            else:
                print("Некорректный ввод! Пожалуйста, выберите действие от 1 до 4")

if __name__ == "__main__":
    app = TornadoApp()
