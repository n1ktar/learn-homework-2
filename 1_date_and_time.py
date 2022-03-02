import locale
from datetime import date, datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    delta_day = timedelta(days=1)
    delta_mouth = timedelta(days=30)
    dt_yerstarday = dt_now - delta_day
    dt_mouth = dt_now - delta_mouth
    print(f'Вчера было {dt_yerstarday}')
    print(f'Сегодня {dt_now}')
    print(f'Месяц назад было {dt_mouth}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
