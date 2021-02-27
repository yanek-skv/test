#pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

##print (html)

#передаём код в BeautifulSoup 1html 2 способ парсинга (html)
soup = BeautifulSoup(html, 'html.parser')
##print(soup)


#запрашиваем класс и ли find_all ищит все find только одно совпадение
news = soup.find_all('li', class_='liga-news-item')
##print(news)

##for i in news:
##    print(i, '\n\n')

results = []

#забираем нужные элементы с нужным текстом с помощью get_text выдёргиваем текст
for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    #создаём список словарей
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

    ##print(title, desc, '\n', href, '\n\n')

# сохраняем всё в файл
f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
    i += 1
f.close()