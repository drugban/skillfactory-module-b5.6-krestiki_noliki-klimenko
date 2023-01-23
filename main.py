field = [['-']*3 for _ in range(3)]
print('Привет, добро пожаловать в игру "Крестики-Нолики"')

def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))

def users_input(f):
    while True:
        place = input("Введите координаты двумя цифрами: ").split()
        if len(place) != 2:
            print("Нужно ввести 2 коррдинаты: ")
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Мы вышли за пределы поля')
            continue
        if f[x][y] != '-':
            print('Клетка уже занята')
            continue
        break
    return x, y

def win(f, user):
    win_coord = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                 ((0,2), (1,1), (2,0)), ((0,0), (1,1), (2,2)), ((0,0), (1,0), (2,0)),
                 ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [user, user, user]:
            return True
    return False

count = 0
while True:
    if count %2 == 0:
        user = 'X'
    else:
        user = 'O'
    show_field(field)
    x, y = users_input(field)
    field[x][y] = user
    if count == 9:
        print('У вас ничья')
    if win(field, user):
        print(f"Выиграл {user}")
        show_field(field)
        break
    count += 1
