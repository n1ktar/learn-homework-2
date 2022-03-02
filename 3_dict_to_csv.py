import csv


dict = [
        {'name': 'Alex', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'John', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Edward', 'age': 48, 'job': 'Big boss'},
        {'name': 'Anna', 'age': 27, 'job': 'Manager'}
    ]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('dict.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dict:
            writer.writerow(user)    

if __name__ == "__main__":
    main()
