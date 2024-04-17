import requests
import re
from bs4 import BeautifulSoup

from database import Database


def fetcher():
    DB = Database()
    DB.connect_to_database()

    PATH = 'https://www.truecar.com/used-cars-for-sale/listings/'

    page = 1
    while True:
        res = requests.get(PATH + '?page=' + str(page))
        if res.status_code == 404:
            print('Last Page : ', page - 1)
            break

        soup = BeautifulSoup(res.text, 'html.parser')
        all_cars_content = soup.find_all('div', attrs={'class': 'card-content order-3 vehicle-card-body'})
        for c in all_cars_content:
            n = c.findNext('div', attrs={'class': 'truncate'})
            name = n.findNext('span', attrs={'class': 'truncate'}).text

            p = c.findNext('div', attrs={'class': 'vehicle-card-bottom-pricing-secondary'})
            q = p.text.split('$')
            # to get price after Off
            price = float(q[-1].replace(',', '.')) if len(q) > 0 else None

            m = c.findNext('div', attrs={'class': 'truncate', 'data-test': 'vehicleMileage'})
            x = re.findall(r'^[\d,]*', m.text)
            mileage = int(x[0].replace(',', ''))

            query = f"INSERT INTO {Database.TABLE_NAME} VALUES ({name}, {price}, {mileage})"
            # print(query)
            DB.execute_query(query)

    DB.close()
