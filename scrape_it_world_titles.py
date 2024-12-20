import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://www.it-world.ru/lenta/'

def get_page_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Ошибка при запросе страницы {url}")
        return []
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    titles_data = []
    articles = soup.find_all('a')

    for article in articles:
        title = article.get_text(strip=True)
        if title:
            titles_data.append([title])
    return titles_data

def collect_all_titles():
    url = base_url
    return get_page_data(url)

def save_to_csv(data, filename='it_world_titles.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        writer.writerows(data)

if __name__ == '__main__':
    titles = collect_all_titles() 
    save_to_csv(titles) 
    print("Done!")
