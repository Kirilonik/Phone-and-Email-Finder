#! python3
# ! phoneEmail - Находит телефонные номера и
# адреса электронной почты в буфере обмена.

import pyperclip
import re

# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?   # территориальный код
# (\s|-|\.)?           # разделитель
# (\d{3})              # первые 3 цифры
# (\s|-|\.)            # разделитель
# (\d{4})              # последние 4 цифры
# )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # имя пользователя
    @                       # Символ
    [a-zA-Z0-9.-]+          # имя домена
    (\.[a-zA-Z]{2,4})       # Остальная часть адреса
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
# for group in phoneRegex.findall(text):
#    phoneNum = '-'.join([group[1], group[3], group[5]])
#    matches.append(phoneNum)

for group in emailRegex.findall(text):
    matches.append(group[0])

# Копирование результатов в буфер обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Скопированно в буфер обмена:")
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены...')
