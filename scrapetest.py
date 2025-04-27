# стандартная библиотека python
from urllib.request import urlopen
from bs4 import BeautifulSoup

# функция urlopen открывает удаленный объект по сети и читает его
html = urlopen('http://pythonscraping.com/pages/page1.html')
#print(html.read())
#bs = BeautifulSoup(html.read(), 'html.parser')

# Здесь контент HTML-файла преобразуется в объект BeautifulSoup
# Первый аргумент - текст в формате HTML, второй - синтаксический анализатор,
# который bs4 использует для построения объекта
bs = BeautifulSoup(html, 'html.parser')

# эти три вызова приведут к одинаковому результату
print(bs.title)
print(bs.html.head.title)
print(bs.head.title)

# lxml - тоже синтаксический анализатор, который лучше справляется с
# грязным/искаженным HTML-кодом
#		bslxml = BeautifulSoup(html, 'lxml')
#		print(bslxml.h1)

