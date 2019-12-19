#! python3
# ! phoneEmail - Находит телефонные номера и
# адреса электронной почты в буфере обмена.

import pyperclip
import re

# Создаем шаблон для 2-х разных видов номеров.
phoneRegex = re.compile(r'\d{3}.*?\d{3}.*?\d{2}.*?\d{2}')

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # имя пользователя
    @                       # Символ
    [a-zA-Z0-9.-]+          # имя домена
    (\.[a-zA-Z]{2,4})       # Остальная часть адреса
)''', re.VERBOSE)


text = str(pyperclip.paste())

phones = []
emails = []
for group in phoneRegex.findall(text):
    phones.append(group)

for group in emailRegex.findall(text):
    emails.append(group[0])

# Копирование результатов в буфер обмена.

if len(emails) == 0:
    print("\n Email не найдены...")
if len(phones) == 0:
    print("\n Mobile phone numbers не найдены...")

phones.extend(emails)

if len(phones) > 0:
    pyperclip.copy('\n'.join(phones))
    print("\nСкопированно в буфер обмена:")
    print('\n'.join(phones))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены...')
