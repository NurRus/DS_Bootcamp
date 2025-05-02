#!/usr/bin/env python

import sys
import time
import requests
from bs4 import BeautifulSoup

def get_financial_data(ticker, field):

    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"

    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе страницы: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')

    financial_block = soup.find('div', {'class':'row lv-0 yf-t22klz'})
    if not financial_block:
        raise Exception(f"Блок с финансовыми данными для тикера '{ticker}' не найден.")
    
    row = financial_block.find('div', {'title':field})
    if not row:
        raise Exception(f"Поде '{field}' не найдено в таблице.")
    
    data = []
    data.append(field)
    for index, cell in enumerate(row.find_all_next('div')):
        if index >= 5:  # Останавливаемся после 5 значений
            break
        data.append(cell.text.strip())

    return tuple(data)


def main():
    if len(sys.argv) != 3:
        print("Использование: ./financial.py <тикер> <поле>")
        sys.exit(1)
    
    ticker = sys.argv[1]
    field  = sys.argv[2]

    # Пауза 5 сек
    time.sleep(5)

    try:
        data = get_financial_data(ticker, field)
        print(data)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

