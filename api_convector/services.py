import random
import bs4
import requests


def returns_random_photo(text):
    """Возвращает рандомную фотографию по фильтру в названии запроса"""
    url = f'https://www.istockphoto.com/ru/search/2/image?phrase={text}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9 '
    }
    response = requests.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    max_number_pagination = soup.find('span', class_='PaginationRow-module__lastPage___q1Bw1')
    if max_number_pagination:
        number_page = random.randint(1, int(max_number_pagination.text))
        url = f'https://www.istockphoto.com/ru/search/2/image?phrase={text}&page={number_page}'
        response = requests.get(url=url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        photos = soup.find_all("div", class_="MosaicAsset-module__galleryMosaicAsset___Nt_YP")
        random_number_photo = random.randint(1, len(photos) - 1)
        photo = photos[random_number_photo].find('source').get('srcset')
        return {'link': photo}
    else:
        return {'error': 'Sorry, there are no such photos'}
