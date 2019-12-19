#! python3
# ! phoneEmail - Находит телефонные номера и
# адреса электронной почты в буфере обмена.

import pyperclip
import re

# Создаем шаблон для 2-х разных видов номеров.
phoneRegex = re.compile(r'''[+7]\d{10} | \d{11}''')


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
if len(phones) > 0:
    pyperclip.copy('\n'.join(phones))
    print("Скопированно в буфер обмена:")
    print('\n'.join(phones))
if len(emails) > 0:
    pyperclip.copy('\n'.join(emails))
    print("\nСкопированно Email в буфер обмена:")
    print('\n'.join(emails))

else:
    print('Телефонные номера и адреса электронной почты не обнаружены...')
