import pytest
import financial  # Импортируем ваш основной скрипт

def test_get_financial_data_total_revenue():
    ticker = "MSFT"
    field = "Total Revenue"

    # Вызываем функцию и проверяем, что она возвращает данные
    data = financial.get_financial_data(ticker, field)
    assert data is not None
    assert data[0] == field
    assert len(data) == 6  # Предполагаем, что возвращается 5 значений плюс название поля

def test_get_financial_data_return_type():
    ticker = "MSFT"
    field = "Total Revenue"

    # Вызываем функцию и проверяем тип возвращаемого значения
    data = financial.get_financial_data(ticker, field)
    assert isinstance(data, tuple)

def test_get_financial_data_invalid_ticker():
    ticker = "INVALID"
    field = "Total Revenue"

    # Проверяем, что вызывается исключение при недействительном тикере
    with pytest.raises(Exception, match="Блок с финансовыми данными для тикера 'INVALID' не найден."):
        financial.get_financial_data(ticker, field)
