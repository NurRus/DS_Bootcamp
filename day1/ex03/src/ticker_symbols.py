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

def get_stock_price(ticker):
    # Проверяем, есть ли компания в словаре COMPANIES
    if ticker in STOCKS:
        stock_price = STOCKS.get(ticker, "Unknown company")
        return stock_price
    else:
        return "Unknown company"
    
def get_name_company(ticker):
    for name in COMPANIES:
        if COMPANIES[name] == ticker:
            return name
    return "Unknown company"

def main():
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        return

    # Получаем название компании из аргументов
    ticker = sys.argv[1].upper()

    # Получаем цену акций
    stock_price = get_stock_price(ticker)

    if stock_price == "Unknown company":
        print(stock_price)
        return
 
    company_name = get_name_company(ticker)
    print(company_name + " " + str(stock_price))
 

if __name__ == '__main__':
    main()
