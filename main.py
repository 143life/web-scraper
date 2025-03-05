from bs4 import BeautifulSoup
with open("../git-resources/scrap_tutorial/lesson1/blank/index.html") as file:
    src = file.read()


# передача в конструктор класса html-кода страницы
# конструктор строит из него набор объектов
soup = BeautifulSoup(src, "lxml")
title = soup.title
print(title.text)
print(title.string)

# find и find_all

page_h1 = soup.find("h1")
print(page_h1.text)
page_h1_all = soup.find_all("h1")
for i in page_h1_all:
    print(i.string)

user_name = soup.find("div", class_ = "user__name")
print(user_name.text.strip())

user_name = soup.find("div", class_="user__name").find("span").text
print(user_name)

user_name = soup.find("div", {"class": "user__name", "id": 
    "aaa"}).find("span").text
print(user_name)

user_info = soup.find("div", class_="user__info").find_all("span")
for i in user_info:
    print(i.string.strip())


social_networks = soup.find("div", class_="social__networks").find_all("a")
for i in social_networks:
    print(i.text)

all_a = soup.find_all("a")
for i in all_a:
    print(i)

for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")

# .find_parent() and .find_parents()

post_div = soup.find("div", class_="post__text").find_parent()
print(post_div)

post_div = soup.find("div", class_="post__text").find_parent("div", "user__post")
print(post_div)

post_divs = soup.find(class_="post__text").find_parents()
print(post_divs)

# .next_element() and .previous_element()

next_el = soup.find(class_="post__title").next_element.next_element
print(next_el)

next_el = soup.find(class_="post__title").find_next().text
print(next_el)