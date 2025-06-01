#esli na rabatet vot biblioteki: pip install googletrans==4.0.0-rc1

import datetime
import webbrowser
import time
import sys
from deep_translator import GoogleTranslator 
import ctypes
import os

def greet_user():


    print("Artem PIDOR!!!")

    print("Hello! I'm your assistant bot.")
    print("I can help you with the following commands:")
    print("- time")
    print("- date")
    print("- calculator")
    print("- search")
    print("- remind")
    print("- translate")  
    print("- exit")

def get_time():
    now = datetime.datetime.now()
    print("Current time:", now.strftime("%H:%M:%S"))

def get_date():
    today = datetime.date.today()
    print("Today's date:", today.strftime("%d.%m.%Y"))

def calculator():
    print("Enter an expression (5 + 3):")
    expr = input(">>> ")
    try:
        result = eval(expr)
        print("Result:", result)
    except:
        print("Invalid expression.")

def search_google():
    query = input("What do you want to search for on Google? ")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    print("Opening browser...")

def reminder():
    text = input("What should I remind you of? ")
    seconds = int(input("In how many seconds should I remind you? "))
    print(f"Okay, I'll remind you in {seconds} seconds.")
    time.sleep(seconds)
    print(f"REMINDER: {text}")

def translate_text():
    text = input("Enter text to translate: ")
    lang = input("Translate to which language? ('ru', 'en'): ").strip()
    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        print(f"Translation: {translated}")
    except Exception as e:
        print("Translation failed:", str(e))

#def show_error_box(title, message):
    #ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)

def main():
    greet_user()
    while True:
        command = input("\nEnter command: ").lower()
        if command == "time":
            get_time()
        elif command == "date":
            get_date()
        elif command == "calculator":
            calculator()
        elif command == "search":
            search_google()
        elif command == "remind":
            reminder()
        elif command == "translate":
            translate_text()  
        elif command == "exit":
            print("Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()