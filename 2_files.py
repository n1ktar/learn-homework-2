

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        referat = f.read()
        print(len(referat))
        print(len(referat.split()))
        referat = referat.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as b:
        b.write(referat)

if __name__ == "__main__":
    main()
