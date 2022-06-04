import csv
from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_term):
    template = 'https://www.amazon.ca/s?k={}'
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    url += '&page={}'
    return url


def extract_record(item):
    a_tag = item.h2.a
    description = a_tag.text.strip()
    url = 'https://www.amazon.ca' + a_tag.get('href')

    try:
        sponsored_parent = item.find('span', {'class': 'a-declarative'})
        sponsored = sponsored_parent.find('span', 'a-color-base').text
    except AttributeError:
        try:
            price_discount_parent = item.find('span', 'a-price a-text-price')
            previous_price = price_discount_parent.find('span', 'a-offscreen').text
        except AttributeError:
            previous_price = ''
        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
        except AttributeError:
            return
        try:
            rating = item.i.text
            if len(item.find('span', {'class': 'a-size-base'}).text) < 9:
                review_count = item.find('span', {'class': 'a-size-base'}).text
            else:
                review_count = 0
                rating = 'No reviews'
        except AttributeError:
            rating = 'No reviews'
            review_count = '0'

        if previous_price == '':
            percent_discount = '0%'
        else:
            percent_discount = round(((float(price[1:].replace(",", "")) - float(
                previous_price[1:].replace(",", ""))) / float(previous_price[1:].replace(",", ""))) * 100, 2)
            percent_discount = f"{percent_discount}%"

        result = (description, previous_price, price, percent_discount, rating, review_count, url)
        return result


def main(search_term):
    driver = webdriver.Chrome("C:\Development\chromedriver.exe")
    records = []
    url = get_url(search_term)

    for page in range(1, 8):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            print(record)
            if record:
                records.append(record)
    driver.close()
    with open(f'{search}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price Was', 'Price', 'Percent Off', 'Rating', 'Review Count', 'URL'])
        writer.writerows(records)


search = input("Search term: ")
main(search)
