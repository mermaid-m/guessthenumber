import random, time
import sqlite3

print('Здравствуйте. Я загадываю число, дайте время подумать ...')
time.sleep(3)
print('Ооо, Я придумал! У вас 5 попыток.')
randomizer = random.randint(1, 10)
attempts = 0

#процесс игры
for attempts in range(5):
    g_number = int(input('Угадайте число от 1 до 10, у вас 5 попыток: '))
    if g_number > randomizer:
        print('Ваше число велико, попробуйте снова.')
    if g_number < randomizer:
        print('Ваше число мало, попробуйте снова.')
    if g_number == randomizer:
        print(f'Вы угадали за {attempts} попыток! Поздравляю!')
        break
else:
    print('Вы не угадали и попытки закончились, не расстраивайтесь.')

#создаю базу данных
con_db = sqlite3.connect('players.db')
cur = con_db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS players(
    name TEXT,
    count_att INTEGER);
''')
con_db.commit()
#добавляю данные в базу данных
pl = str(input('Введите имя: '))
data_tuple = (pl, attempts)

cur.execute('''INSERT INTO players
            VALUES (?, ?)''', data_tuple) #запрос на вставку в БД
con_db.commit() #сохранение


#вывод из таблиццы результатов играков
cur.execute('SELECT * FROM players;')
all_results = cur.fetchall()
print(all_results)
con_db.close() #закрыть соеденение с БД

