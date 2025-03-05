import os
import subprocess
import time
import elevate
import sys

# Запуск службы PostgreSQL
print("Starting PostgreSQL service...")
# if not elevate.elevate(show_console=True):
#     print("Не удалось получить права администратора.")
#     sys.exit(1)
#
# print("Скрипт запущен от имени администратора!")
# # Ваш код здесь
subprocess.run(["net", "start", "postgresql-x64-17"])

# Подождите некоторое время, пока служба запустится
time.sleep(5)

# Запуск Django-проекта
print("Starting Django project...")
os.system("python manage.py runserver")