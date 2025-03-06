import os
from PyPDF2 import PdfReader
import pdfplumber


def extract_pdf_data(file_path):
    try:
        # Открываем PDF-файл
        reader = PdfReader(file_path)

        # Извлекаем метаданные
        metadata = reader.metadata
        title = metadata.get('/Title', 'Без заголовка')  # Заголовок
        authors = metadata.get('/Author', '').split(',')  # Авторы
        year = metadata.get('/CreationDate', None)  # Год создания

        # Извлекаем текст
        content = ''
        for page in reader.pages:
            content += page.extract_text() or ''

        return {
            'title': title.strip(),
            'authors': [author.strip() for author in authors],
            'year': int(year[:4]) if year and year[:4].isdigit() else None,
            'content': content.strip(),
            'file_path': os.path.abspath(file_path),  # Абсолютный путь к файлу
        }
    except Exception as e:
        raise ValueError(f"Ошибка при обработке PDF: {e}")


def extract_pdf_title_from_text(file_path):
    with pdfplumber.open(file_path) as pdf:
        # Читаем первый страницу
        first_page = pdf.pages[0]
        text = first_page.extract_text()  # Извлекаем текст

        # Простая логика для поиска заголовка
        if text:
            lines = text.split('\n')
            title = lines[0].strip() if lines else 'Нет заголовка'
        else:
            title = 'Нет заголовка'

    file_path = os.path.abspath(file_path)
    return {
        'title': title,
        'file_path': file_path
    }
