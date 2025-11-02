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
            print("3. Настройки")
            print("4. Выход")
            
            choice = input("\nВыберите действие: ")
            
            if choice == "1":
                self.decrypt()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.settings()
            elif choice == "4":
                print("Завершение работы...")
                time.sleep(1)
                sys.exit()
            else:
                print("Некорректный ввод! Пожалуйста, выберите действие от 1 до 4")

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
        
        query = input("Введите поисковый запрос: ").strip()
        
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
