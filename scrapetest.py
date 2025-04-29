# стандартная библиотека python
from urllib.request import urlopen
# HTTPError - сервер выдает код не 200
# URLError - сервер не найден (о как)
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

URLS = [
	'http://pythonscraping.com/pages/page1.html'
]

def get_title(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	doc = BeautifulSoup(html, 'html.parser')
	try:
		title = doc.title
	except AttributeError as e:
		return None
	return title

title = get_title(URLS[0])
if title == None:
	print('Tag was not found')
else:
	print(title)

# функция urlopen открывает удаленный объект по сети и читает его
try:
	html = urlopen(URLS[0])
except HTTPError as e:
	# оборачиваем в обработку исключения на случай, если не код 200
	print(e)
except URLError as e:
	# если не найден сервер
	print(e)
else:

#print(html.read())
#bs = BeautifulSoup(html.read(), 'html.parser')

# Здесь контент HTML-файла преобразуется в объект BeautifulSoup
# Первый аргумент - текст в формате HTML, второй - синтаксический анализатор,
# который bs4 использует для построения объекта
	bs = BeautifulSoup(html, 'html.parser')

# эти три вызова приведут к одинаковому результату
	print('\n'+bs.title.__str__()) # \n не в счет конечно же
	print(bs.html.head.title)
	print(bs.head.title)
	try:
		attr = bs.z.z
		# bs.z = None, => bs.z.z вызовет exception AttributeError
	except AttributeError as e:
		print(e)
	else:
		if attr == None:
			print('Tag was not found')
		else:
			print(attr)

# lxml - тоже синтаксический анализатор, который лучше справляется с
# грязным/искаженным HTML-кодом
#		bslxml = BeautifulSoup(html, 'lxml')
#		print(bslxml.h1)
# также есть html5lib - еще круче, но медленнее