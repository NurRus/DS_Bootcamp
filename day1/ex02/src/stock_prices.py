import sys

# Определение словарей
COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
}

STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
}

def get_stock_price(company_name):
    # Проверяем, есть ли компания в словаре COMPANIES
    if company_name in COMPANIES:
        # Получаем тикер компании
        ticker = COMPANIES[company_name]
        # Получаем цену акций по тикеру
        stock_price = STOCKS.get(ticker, "Unknown company")
        return stock_price
    else:
        return "Unknown company"

def main():
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        return

    # Получаем название компании из аргументов
    company_name = sys.argv[1].capitalize()

    # Получаем цену акций
    stock_price = get_stock_price(company_name)

    # Выводим цену акций
    print(stock_price)

if __name__ == '__main__':
    main()
