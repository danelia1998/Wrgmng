import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

# Создание дата-класса для языков программирования
@dataclass
class Language:
    name: str
    popularity: int
    category_front: str
    category_back: str

# Функция для получения данных из таблицы
def get_languages():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable sortable")
    rows = table.tbody.find_all("tr")
    languages = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 3:
            name = cells[0].get_text().strip()
            try:
                popularity = int(cells[1].get_text().strip().replace(',', ''))
            except ValueError:
                splitter = cells[1].get_text().strip().replace(',', '').replace('.', '').split('(', 1)
                popularity = splitter[0]
                continue
            category_front = cells[2].get_text().replace(",", "").strip()
            category_back = cells[3].get_text().replace(",", "").strip()
            language = Language(name, popularity, category_front, category_back)
            languages.append(language)
    return languages
