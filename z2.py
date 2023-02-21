from z1 import Technic


if __name__ == '__main__':
    a = Technic(name='Планшет', price=10000, availability=True)
    b = Technic(name='Телевизор', price=50000, availability=True)
    c = Technic(name='Телефон', price=4000, availability=True)
    print(a.name, b.name, 'сравнение (<)', a < b)
    print(a.name, b.name, 'сравнение (>)', a > b)
    print(a.name, b.name, 'сравнение (<=)', a <= b)
    print(a.name, c.name, 'сравнение (>=)', a >= c)
    print(a.name, c.name, 'сравнение (==)', a == c)
    print(a.name, b.name, 'сравнение (!=)', a != b)
