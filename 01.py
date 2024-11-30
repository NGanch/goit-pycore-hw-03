# Завдання 1
from datetime import datetime

def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        difference = (given_date - current_date).days
        return difference
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    
print(get_days_from_today("2023-03-14"))
print(get_days_from_today("2025-05-01"))
print(get_days_from_today("неправильна дата"))

