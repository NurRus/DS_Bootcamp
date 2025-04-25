import sys

# Словари компаний и акций
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

def get_stock_info(expression):
    # Приводим первый символ к верхнему регистру, остальные — к нижнему
    normalized_expression = expression.strip().capitalize()
    if normalized_expression in COMPANIES:
        ticker = COMPANIES[normalized_expression]
        stock_price = STOCKS.get(ticker, "unknown")
        return f"{normalized_expression} stock price is {stock_price}"
    else:
        # Приводим все символы к верхнему регистру
        upper_expression = expression.strip().upper()
        if upper_expression in COMPANIES.values():
            for company, ticker in COMPANIES.items():
                if ticker == upper_expression:
                    return f"{upper_expression} is a ticker symbol for {company}"
        else:
            return f"{expression.strip()} is an unknown company or an unknown ticker symbol"

def main():
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]
    if ',, ' in input_string or ', ,' in input_string:
        return

    expressions = input_string.split(',')
    for expression in expressions:
        expression = expression.strip()
        if expression:
            result = get_stock_info(expression)
            print(result)

if __name__ == '__main__':
    main()
